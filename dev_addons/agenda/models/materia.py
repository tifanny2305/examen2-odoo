
from odoo import models, fields

class Materia(models.Model):
    _name = 'agenda.materia'
    _description = 'Materia'
    _rec_name = 'nombre'

    nombre = fields.Char(string="Nombre")
    curso_ids = fields.Many2many('agenda.curso', 'cursomateria', 'materia_id', 'curso_id',  string="Cursos")
