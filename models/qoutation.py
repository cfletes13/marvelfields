# -*- coding: utf-8 -*-
from odoo import fields, models


class QoutationClasificacion(models.Model):
    _inherit = 'sale.order'
    qou_clas = fields.Many2many(related='partner_id.clasificaciones_ids',
                                string="Clasificacion", readonly=True)


class QoutationSubclase(models.Model):
    _inherit = 'sale.order'
    qou_subclase = fields.Many2many(related='partner_id.subclases_ids',
                                    string="Subclase", readonly=True)
