
from odoo import models, fields, api

class Calendar(models.Model):
    _inherit = 'calendar.event'

    custom_field = fields.Char(string="Custom Field")
    curso_ids = fields.Many2many('agenda.curso', string="Cursos")
    comunicado_id = fields.Many2one('agenda.comunicado', string="Comunicado")
    actividad_id = fields.Many2one('agenda.actividad', string="Actividad")
    archivo_ids = fields.One2many('agenda.archivo', compute='_compute_archivo_ids', string="Archivos Adjuntos", store=False)

    @api.depends('comunicado_id')
    def _compute_archivo_ids(self):
        for event in self:
            event.archivo_ids = event.comunicado_id.archivo_ids

    def write(self, vals):

        if not self.env.context.get('from_comunicado_write'):
            for event in self:
                if event.comunicado_id:
                    update_vals = {}
                    if 'name' in vals:
                        update_vals['nombre'] = vals['name']
                    if 'start' in vals:
                        update_vals['fecha_inicio'] = vals['start']
                    if 'stop' in vals:
                        update_vals['fecha_fin'] = vals['stop']
                    if 'description' in vals:
                        update_vals['descripcion'] = vals['description']
                    if 'curso_ids' in vals:
                        update_vals['curso_ids'] = [(6, 0, event.curso_ids.ids)]

                    if update_vals:
                        event.comunicado_id.with_context(from_event_write=True).write(update_vals)

        return super(Calendar, self).write(vals)