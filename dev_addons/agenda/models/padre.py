from odoo import models, fields, api

class Padre(models.Model):
    _name = 'agenda.padre'
    _description = 'Padre'

    user_id = fields.Many2one('res.users', string='Usuario', required=True)
    estudiante_ids = fields.One2many('agenda.estudiante', 'padre_id', string="Estudiante")
    direccion = fields.Char(string="Dirección")
    telefono = fields.Char(string="Teléfono")
    sexo = fields.Selection([('masculino', 'Masculino'), ('femenino', 'Femenino')], string="Sexo")

    @api.model
    def create(self, vals):
        # Crear el usuario usando el método original
        user_vals = {
            'name': vals.get('user_id'),
            'login': vals.get('user_id') + '@example.com',
            'password': 'password',
            roles
