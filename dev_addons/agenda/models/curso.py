from odoo import models, fields

class curso(models.Model):
    _name = 'agenda.curso'
    _description = 'curso'

    name = fields.Char(string = "Nombre de la Curso", required = True)
    materia_id = fields.Many2many('agenda.materia', 'curso_materia_rel', 'curso_id', 
                                    'materia_id', string = "materias")