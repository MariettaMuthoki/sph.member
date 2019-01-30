# -*- coding: utf-8 -*-
{
    'name': "sph members",

    'summary': """
        Swahilipot member registration portal""",

    'description': """
        A community of techies and artists.
    """,

    'author': "Marietta",
    'website': "http://www.swahilipothub.co.ke",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full l
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
         'views/sphmember_view.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
