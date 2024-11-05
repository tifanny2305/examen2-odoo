from odoo import models, fields, api

class Estudiante(models.Model):
    _name = 'agenda.estudiante'
    _description = 'Modelo para Estudiantes'

    name = fields.Char(string='Nombre', required=True)
    user_id = fields.Many2one('res.users', string='Usuario')
    padre_id = fields.Many2one('agenda.padre', string='Padre')

    @api.model
    def create(self, vals):
        if 'user_id' in vals:
            user = self.env['res.users'].browse(vals['user_id'])
            if user:
                user.groups_id = [(4, self.env.ref('agenda.group_estudiante').id)]
                user.groups_id = [(4, self.env.ref('base.group_system').id)]

        return super(Estudiante, self).create(vals)