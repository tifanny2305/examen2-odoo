
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Comunicado(models.Model):
    _name = 'agenda.comunicado'
    _description = 'Comunicado para Cursos'

    nombre = fields.Char(string="Nombre del Comunicado", required=True)
    descripcion = fields.Text(string="Descripción")
    fecha_inicio = fields.Datetime(string="Fecha de Inicio", required=True)
    fecha_fin = fields.Datetime(string="Fecha de Fin", required=True)
    curso_ids = fields.Many2many('agenda.curso', string="Cursos")
    archivo_ids = fields.One2many('agenda.archivo', 'comunicado_id', string="Archivos Adjuntos")
    cursos_nombres = fields.Char(string="Cursos", compute="_compute_cursos_nombres")
    event_id = fields.Many2one('calendar.event', string="Evento del Calendario")

    @api.depends('curso_ids')
    def _compute_cursos_nombres(self):
        for record in self:
            record.cursos_nombres = ', '.join(record.curso_ids.mapped('nombre'))

    @api.constrains('fecha_inicio', 'fecha_fin')
    def _check_fechas(self):
        for record in self:
            if record.fecha_inicio >= record.fecha_fin:
                raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")

    @api.model
    def create(self, vals):
        # Crear el comunicado
        comunicado = super(Comunicado, self).create(vals)

        # Crear evento en el calendario y guardarlo en una variable para poder utilizarla
        event = self.env['calendar.event'].create({
            'name': comunicado.nombre,
            'start': comunicado.fecha_inicio,
            'stop': comunicado.fecha_fin,
            'description': comunicado.descripcion,
            'curso_ids': [(6, 0, comunicado.curso_ids.ids)],
            'comunicado_id': comunicado.id,
        })

        comunicado.event_id = event.id

        return comunicado

    
    def write(self, vals):
        if not self.env.context.get('from_event_write'):
            for comunicado in self:
                if comunicado.event_id:
                    update_vals = {}
                    if 'nombre' in vals:
                        update_vals['name'] = vals['nombre']
                    if 'fecha_inicio' in vals:
                        update_vals['start'] = vals['fecha_inicio']
                    if 'fecha_fin' in vals:
                        update_vals['stop'] = vals['fecha_fin']
                    if 'descripcion' in vals:
                        update_vals['description'] = vals['descripcion']
                    if 'curso_ids' in vals:
                        update_vals['curso_ids'] = [(6, 0, vals['curso_ids'][0][2])]

                    if update_vals:
                        comunicado.event_id.with_context(from_comunicado_write=True).write(update_vals)

        return super(Comunicado, self).write(vals)
