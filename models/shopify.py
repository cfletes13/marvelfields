# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductTemplateShopify(models.Model):
    _inherit = "product.template"

    image_shopify = fields.Binary(string='Imagen Sopify',
                                  store=True, attachment=True)

    website_shopify = fields.Boolean(default=False,
                                     string='Website Shopify')


class SaleOrderShopify(models.Model):
    _inherit = "sale.order"

    metodo_de_pago = fields.Char(string='Metodo de Pago',)
    metodo_de_envio_shopify = fields.Char(string='Metodo de Envio Shopify')
    pago_con_gift_cards = fields.Boolean(default=False,
                                         string='Pago con Gift Cards')
