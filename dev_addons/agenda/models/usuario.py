
from odoo import models, fields

class Usuario(models.Model):
    _inherit = 'res.users'

    profesor_ids = fields.One2many('agenda.profesor', 'user_id', string="Profesores")
    tutor_ids = fields.One2many('agenda.padre', 'user_id', string="Padres")
    admin_ids = fields.One2many('agenda.administrativo', 'user_id', string="Administrador")
    estudiante_ids = fields.One2many('agenda.estudiante', 'user_id', string="Estudiantes")

    def create_user_with_role(self, vals, role):
        # Crear el usuario usando los valores proporcionados
        user = self.create(vals)
        
        # Asignar el grupo según el rol proporcionado
        if role == 'profesor':
            group = self.env.ref('agenda.group_profesor')
        elif role == 'estudiante':
            group = self.env.ref('agenda.group_estudiante')
        elif role == 'padre':
            group = self.env.ref('agenda.group_padre')
        elif role == 'administrativo':
            group = self.env.ref('agenda.group_admin')
        else:
            group = None

        if group:
            user.groups_id = [(4, group.id)]

        return user
