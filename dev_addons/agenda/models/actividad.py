from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Actividad(models.Model):
    _name = 'agenda.actividad'
    _description = 'Actividad'

    nombre = fields.Char(string="Nombre", required=True)
    fecha_ini = fields.Datetime(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Datetime(string="Fecha de Fin", required=True)
    descripcion = fields.Text(string="Descripción")
    nota = fields.Float(string="Nota")

    cursos_nombres = fields.Char(string="Cursos", compute="_compute_cursos_nombres")
    event_id = fields.Many2one('calendar.event', string="Evento del Calendario")
    curso_ids = fields.Many2many('agenda.curso', string="Cursos")
    estudiante_id = fields.Many2one('agenda.estudiante', string="Estudiante", ondelete="cascade")
    #periodo_id = fields.Many2one('agenda.periodo', string="Periodo", ondelete="cascade")
    archivo_ids = fields.One2many('agenda.archivo', 'actividad_id', string="Archivos Adjuntos")

    @api.depends('curso_ids')
    def _compute_cursos_nombres(self):
        for record in self:
            record.cursos_nombres = ', '.join(record.curso_ids.mapped('nombre'))

    @api.constrains('fecha_ini', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_ini >= record.fecha_fin:
                raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")

    @api.model
    def create(self, vals):
        # Crear la actividad
        actividad = super(Actividad, self).create(vals)

        # Crear evento en el calendario y guardarlo en una variable para poder utilizarla
        event = self.env['calendar.event'].create({
            'name': actividad.nombre,
            'start': actividad.fecha_ini,
            'stop': actividad.fecha_fin,
            'description': actividad.descripcion,
            'curso_ids': [(6, 0, actividad.curso_ids.ids)],
            'actividad_id': actividad.id,
        })

        actividad.event_id = event.id

        return actividad

    
    def write(self, vals):
        if not self.env.context.get('from_event_write'):
            for actividad in self:
                if actividad.event_id:
                    update_vals = {}
                    if 'nombre' in vals:
                        update_vals['name'] = vals['nombre']
                    if 'fecha_ini' in vals:
                        update_vals['start'] = vals['fecha_ini']
                    if 'fecha_fin' in vals:
                        update_vals['stop'] = vals['fecha_fin']
                    if 'descripcion' in vals:
                        update_vals['description'] = vals['descripcion']
                    if 'curso_ids' in vals:
                        update_vals['curso_ids'] = [(6, 0, vals['curso_ids'][0][2])]

                    if update_vals:
                        actividad.event_id.with_context(from_actividad_write=True).write(update_vals)

        return super(Actividad, self).write(vals)