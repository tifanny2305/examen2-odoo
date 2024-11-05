from odoo import models, fields

class materia(models.Model):
    _name = 'agenda.materia'
    _description = 'materia'

    name = fields.Char(string = "Nombre de la Materia", required = True)
    curso_id = fields.Many2many('agenda.curso', 'curso_materia_rel', 
                                        'materia_id', 'curso_id', string = "cursos")