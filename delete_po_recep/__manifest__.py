# -*- coding: utf-8 -*-
{
    'name': 'delete receipts',
    'version': '17.0.1.0',
    'sequence':1,
    'category': '',
    'summary': 'delete receipts',
    'description': 'delete receipts',
    'author': 'Jawad Ali',
    'website': '',
    'depends': ['base_setup','account','sale', 'product', 'purchase', 'stock'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking.xml',
    ],
    'test': [],
    'installable':True,
    'application':True,
    'auto-install':False,
}

