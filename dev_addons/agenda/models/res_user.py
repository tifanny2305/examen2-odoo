from odoo import models, fields


class ResUser(models.Model):
    _inherit = 'res.users'

    profesor_ids = fields.One2many(
        'agenda.profesor', 'user_id', string="Profesores")

    padre_ids = fields.One2many('agenda.padre', 'user_id', string="Padres")

    admin_ids = fields.One2many(
        'agenda.admin', 'user_id', string="Administrador")
        
    estudiante_ids = fields.One2many(
        'agenda.estudiante', 'user_id', string="Estudiantes")

#One2many = uno a muchos

