# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'altaher_code',
    'version' : '1.1',
    'summary': '',
    'sequence': 90,
    'description': """
    """,
    'category': '',
    'website': '',
    'depends' : ['base'],
    'data': [
        'views/code_one.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'post_init_hook': '_auto_install_l10n',
}
