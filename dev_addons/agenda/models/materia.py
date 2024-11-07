
from odoo import models, fields

class Materia(models.Model):
    _name = 'curso.materia'
    _description = 'Materia'

    nombre = fields.Char(string="Nombre")
    cursos = fields.Many2many('curso.materia', 'materia_id',  string="Cursos")
