# -*- coding: utf-8 -*-
from odoo import fields, models

class CrmClaims(models.Model):
    _inherit = 'crm.claim'

    product_tmpl_id = fields.Many2one('product.template',string="Modelo")