# -*- coding: utf-8 -*-
from odoo import fields, models


class ShopifySaleOrder(models.Model):
    _inherit = 'sale.order'
    x_studio_metodo_de_pago = fields.Char(string="Metodo de Pago")
