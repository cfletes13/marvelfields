# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Product(models.Model):
	_inherit = "product.product"

	length = fields.Float(string="Length")
	whidth = fields.Float(string="Whidth")
	high = fields.Float(string="High")

class Template(models.Model):
	_inherit = "product.template"

	length = fields.Float(string="Length", compute='_compute_measures')
	whidth = fields.Float(string="Whidth", compute='_compute_measures')
	high = fields.Float(string="High", compute='_compute_measures')
	temporary_id = fields.Many2one('product.temporary',string="Temporary")
	is_on_catalogue = fields.Boolean(string="Is on Catalogue")

	@api.depends('product_variant_ids','product_variant_ids.length','product_variant_ids.whidth','product_variant_ids.high')
	def _compute_measures(self):
		unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
		for template in unique_variants:
			template.length = template.product_variant_ids.length
			template.whidth = template.product_variant_ids.whidth
			template.high = template.product_variant_ids.high
		for template in (self - unique_variants):
			template.length = 0.0
			template.whidth = 0.0
			template.high = 0.0