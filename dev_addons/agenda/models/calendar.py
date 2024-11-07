from odoo import models, fields

class Calendar(models.Model):
    _inherit = 'calendar.event'

    custom_field = fields.Char(string="Custom Field")
