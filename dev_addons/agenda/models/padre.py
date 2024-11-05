from odoo import models, fields, api

class Padre(models.Model):
    _name = 'agenda.padre'
    _description = 'Modelo Padres'

    name = fields.Char(string='Nombre', required=True)
    user_id = fields.Many2one('res.users', string='Usuario')
    estudiante_ids = fields.One2many('agenda.estudiante', 'padre_id', string='Estudiantes')
    
    @api.model
    def create(self, vals):
        if 'user_id' in vals:
            user = self.env['res.users'].browse(vals['user_id'])
            if user:
                user.groups_id = [(4, self.env.ref('agenda.group_padre').id)]
                user.groups_id = [(4, self.env.ref('base.group_system').id)]
                
        return super(Padre, self).create(vals)