# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_studio_image_shopify = fields.Binary(string='Imagen Sopify',
                                           store=True, attachment=True)

    x_studio_website_shopify = fields.Boolean(default=False,
                                              string='Website Shopify', )


class SaleOrder(models.Model):
    _inherit = "sale.order"

    x_studio_metodo_de_pago = fields.Char(string='Metodo de Pago',)
    x_studio_metodo_de_envio_shopify = fields.Char(string='Metodo de Envio Shopify',)
    x_studio_pago_con_gift_cards = fields.Boolean(default=False,
                                                  string='Pago con Gift Cards', )
