
from odoo import models, fields

class CursoMateria(models.Model):
    _name = 'curso.materia'
    _description = 'Relación entre Curso y Materia'

    curso_id = fields.Many2one('curso.curso', string="Curso", required=True, ondelete='cascade')
    materia_id = fields.Many2one('curso.materia', string="Materia", required=True, ondelete='cascade')
    dia = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes')
    ], string="Día")
    horaInc = fields.Float(string="Hora Inicio")
    horaFin = fields.Float(string="Hora Fin")