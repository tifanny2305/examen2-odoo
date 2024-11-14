
from odoo import models, fields, api

class CargaHoraria(models.Model):
    _name = 'agenda.cargahoraria'
    _description = 'Carga Horaria'

    profesor_id = fields.Many2one('agenda.profesor', string='Profesor', ondelete='cascade')
    materia_ids = fields.Many2many('agenda.materia', string="Materia", required=True)
    curso_ids = fields.Many2many('agenda.curso', string="Cursos")
    anio = fields.Integer(string='Año', required=True)

    # Campos computados para mostrar los nombres
    materia_nombres = fields.Char(string="Materias", compute="_compute_materia_nombres")
    curso_nombres = fields.Char(string="Cursos", compute="_compute_curso_nombres")

    @api.depends('materia_ids')
    def _compute_materia_nombres(self):
        for record in self:
            record.materia_nombres = ', '.join(record.materia_ids.mapped('nombre'))

    @api.depends('curso_ids')
    def _compute_curso_nombres(self):
        for record in self:
            record.curso_nombres = ', '.join(record.curso_ids.mapped('nombre'))