# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Partner(models.Model):
	_inherit = "res.partner"

	payment_days_ids = fields.Many2many('payment.days', 'res_partner_paymnet_days_rel', 'res_partner_id', 'payment_days_id', string="Payment Days")
	collection_executive_id = fields.Many2one("res.users", string="Collection executive")