
from odoo import models, fields, api

class CursoMateria(models.Model):
    _name = 'agenda.cursomateria'
    _description = 'Relación entre Curso y Materia'

    curso_id = fields.Many2one('agenda.curso', string="Curso", required=True, ondelete='cascade')
    materia_id = fields.Many2one('agenda.materia', string="Materia", required=True, ondelete='cascade')
    dia = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes')
    ], string="Día", required=True)
    horaInc = fields.Datetime(string="Hora Inicio", required=True)
    horaFin = fields.Datetime(string="Hora Fin", required=True)

    @api.constrains('horaInc', 'horaFin')
    def _check_horas(self):
        for record in self:
            if record.horaInc >= record.horaFin:
                raise ValidationError("La hora de inicio debe ser anterior a la hora de finalización.")