# -*- coding: utf-8 -*-
{
    'name': "Agenda",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'calendar'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
        'security/group.xml',
        'security/security.xml',
        'views/templates.xml',

        # Vistas
        'views/usuario.xml',
        #'views/administrativo.xml',
        'views/padre.xml',
        'views/estudiante.xml',
        #'views/profesor.xml',
        #'views/actividad.xml',
        'views/comunicado.xml',
        'views/calendar.xml',
        #'views/carga_horaria.xml',
        
        'views/cursomateria.xml',
        'views/curso.xml',
        'views/materia.xml',
        #'views/pagos.xml',
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}

