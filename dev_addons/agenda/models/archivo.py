from odoo import models, fields

class Archivo(models.Model):
    _name = 'agenda.archivo'
    _description = 'Archivo relacionado con Comunicado'

    name = fields.Char(string="Nombre del Archivo", required=True)
    comunicado_id = fields.Many2one('agenda.comunicado', string="Comunicado", ondelete='cascade')
    archivo = fields.Binary(string="Archivo", attachment=True, required=True)
    mimetype = fields.Char(string="Tipo MIME")  # Agregado para almacenar el tipo MIME del archivo