# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Split DO based on planned date(Odoo practical test)',
    'version': '16.0.1.0.0',
    'category': 'Sales/Sales',
    'website': 'https://www.odoo.com',
    'description' : '''
       This module helps to split Do based on sale order line's planned date.
    ''',
    'summary': '''This module helps to split DO based on sale order line's planned date.''',
    'author': 'ODOO Gandhinagar/Trivedi',
    'depends': [
        'sale','sale_stock'
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
    'demo': [],
    'test': [],
    'license': 'LGPL-3',
    'installable' : True,
    'auto_install' : False,
    'application' : True,
    'pre_init_hook': 'pre_init_check',
	
}
