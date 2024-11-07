
from odoo import models, fields

class Curso(models.Model):
    _name = 'curso.curso'
    _description = 'Curso'

    nombre = fields.Char(string="Nombre")
    materias = fields.Many2many('curso.materia', 'curso_id', string="Materias")
