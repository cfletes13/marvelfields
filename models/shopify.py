# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplateShopify(models.Model):
    _inherit = 'product.template'

    image_shopify = fields.Binary(string='Imagen Sopify',
                                  store=True, attachment=True)

    website_shopify = fields.Boolean(default=False,
                                     string='Website Shopify')
