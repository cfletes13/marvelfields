# -*- coding: utf-8 -*-

from odoo import models, fields


class SurtidoSugerido (models.Model):
    _inherit = 'res.partner'

    sugerido = fields.Char(string='Surtido Sugerido',)


class QoutationSurtidoSugerido(models.Model):
    _inherit = 'sale.order'
    qou_sugerido = fields.Char(related='partner_id.sugerido',
                               string="Surtido Sugerido", readonly=True)


class PedidoPortal(models.Model):
    _inherit = 'sale.order'
    portal = fields.Char(string='Pedido Portal', size=6)
