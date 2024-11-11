
from odoo import models, fields

class Estudiante(models.Model):
    _name = 'agenda.estudiante'
    _description = 'Estudiante'

    user_id = fields.Many2one('res.users', string='Usuario', required=True)
    padre_id = fields.Many2one('agenda.padre', string="Padre")
    curso_id = fields.Many2one('agenda.curso', string="Curso")
