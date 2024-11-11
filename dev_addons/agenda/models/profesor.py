
from odoo import models, fields

class Profesor(models.Model):
    _name = 'agenda.profesor'
    _description = 'Profesor'

    user_id = fields.Many2one('res.users', string='Usuario', required=True)
    materias_ids = fields.Many2many('agenda.materia', string='Materias')
