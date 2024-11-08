
from odoo import models, fields

class Curso(models.Model):
    _name = 'agenda.curso'
    _description = 'Curso'

    nombre = fields.Char(string="Nombre")
    tipo = fields.Selection([
        ('primaria', 'Primaria'),
        ('secundaria', 'Secundaria')
    ], string="Tipo", required=True)
    materia_ids = fields.Many2many('agenda.materia', 'cursomateria', 'curso_id', 'materia_id', string="Materias")
