# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PaymentDays(models.Model):
	_name = 'payment.days'

	name = fields.Char(string="Name")