# -*- coding: utf-8 -*-
{
    'name': 'marvelfields',
    'author': 'Marvelsa',
    'website': 'http://www.marvelsa.com',
    'category': 'Uncategorized',
    'version': '1.0.0',
    'depends': ['stock',
                'product',
                'sale',
                'account',
                'sale_stock'
                ],
    'data': [

        # 'views/compatibility.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/clasificaciones.xml',
        'views/subclases.xml',
        'views/clasifica.xml',
        'views/sugerido.xml',
        'views/compatible.xml',
        'views/product_view.xml',
        'views/stock_location.xml',
    ],
}
