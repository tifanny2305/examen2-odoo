from odoo import models, fields

class Archivo(models.Model):
    _name = 'agenda.archivo'
    _description = 'Archivo relacionado con Comunicado'

    name = fields.Char(string="Nombre del Archivo", required=True)
    file = fields.Binary(string="Archivo")
    comunicado_id = fields.Many2one('agenda.comunicado', string="Comunicado", ondelete='cascade')
    mimetype = fields.Char(string="Tipo MIME")  # Agregado para almacenar el tipo MIME del archivo
    actividad_id = fields.Many2one('agenda.actividad', string="Actividad", ondelete="cascade")