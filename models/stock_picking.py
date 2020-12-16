# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockPicking(models.Model):
	_inherit = 'stock.picking'

	delivery_cost = fields.Float(string="Delivery cost")