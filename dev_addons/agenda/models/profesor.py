from odoo import models, fields, api


class Profesor(models.Model):
    _name = 'agenda.profesor'
    _description = 'Modelo Profesor'

    name = fields.Char(string='Nombre', required=True)
    user_id = fields.Many2one('res.users', string='Usuario')

    @api.model
    def create(self, vals):
        if 'user_id' in vals:
            user = self.env['res.users'].browse(vals['user_id'])
            if user:
                user.groups_id = [
                    (4, self.env.ref('agenda.group_profesor').id)]
                user.groups_id = [(4, self.env.ref('base.group_system').id)]

        return super(Profesor, self).create(vals)

#Many2one = muchos a uno