
from odoo import models, fields

class Materia(models.Model):
    _name = 'agenda.materia'
    _description = 'Materia'

    nombre = fields.Char(string="Nombre")
    curso_ids = fields.Many2many('agenda.curso', 'cursomateria', 'materia_id', 'curso_id',  string="Cursos")
