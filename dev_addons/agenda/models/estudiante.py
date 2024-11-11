from odoo import models, fields, api

class Estudiante(models.Model):
    _name = 'agenda.estudiante'
    _description = 'Estudiante'

    name = fields.Char(string='Nombre', required=True)
    email = fields.Char(string='Correo Electrónico', required=True)
    password = fields.Char(string='Contraseña', required=True, default='12345678')
    user_id = fields.Many2one('res.users', string='Usuario', ondelete='cascade')
    padre_id = fields.Many2one('agenda.padre', string="Padre", ondelete='set null')
    curso_id = fields.Many2one('agenda.curso', string="Curso", ondelete='set null')
    is_student = fields.Boolean(string='Es Estudiante', default=True)

    @api.model
    def create(self, vals):
        # Crear el usuario relacionado con el rol 'Estudiante'
        user_vals = {
            'name': vals.get('name'),
            'login': vals.get('email'),
            'password': vals.get('password'),
        }
        user = self.env['res.users'].create(user_vals)

        # Asignar el grupo "Estudiante" al usuario
        group = self.env.ref('agenda.group_estudiante')
        if group:
            user.groups_id = [(4, group.id)]

        # Asociar el usuario recién creado con el registro de `Estudiante`
        vals['user_id'] = user.id
        return super(Estudiante, self).create(vals)

    def write(self, vals):
        # Sincronizar cambios al usuario relacionado si el nombre, correo o contraseña cambian
        if self.user_id:
            user_vals = {}
            if 'name' in vals:
                user_vals['name'] = vals['name']
            if 'email' in vals:
                user_vals['login'] = vals['email']
            if 'password' in vals:
                user_vals['password'] = vals['password']
            if user_vals:
                self.user_id.write(user_vals)

        return super(Estudiante, self).write(vals)

