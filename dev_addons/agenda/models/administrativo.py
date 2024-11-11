
from odoo import models, fields

class Administrativo(models.Model):
    _name = 'agenda.administrativo'
    _description = 'Administrativo'

    user_id = fields.Many2one('res.users', string='Usuario', required=True)
