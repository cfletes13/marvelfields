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
                'sale_stock',
                'sale_margin'
                ],
    'data': [

        # 'views/compatibility.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/payment_days.xml',
        'views/clasificaciones.xml',
        'views/subclases.xml',
        'views/clasifica.xml',
        'views/sugerido.xml',
        'views/compatible.xml',
        'views/product_view.xml',
        'views/stock_location.xml',
        'views/stock_picking.xml',
        'views/temporary.xml',
        'views/payment_days.xml',
        'views/res_partner.xml',
        'data/cron_last_incomming_date.xml',
        'views/sale_order.xml'
    ],
}
