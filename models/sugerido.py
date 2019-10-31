# -*- coding: utf-8 -*-

from odoo import models, fields


class SurtidoSugerido (models.Model):
    _inherit = 'res.partner'

    sugerido = fields.Char(string='Surtido Sugerido',)


class RutaVendedor (models.Model):
    _inherit = 'res.partner'

    rutav = fields.Char(string='Ruta',)


class QoutationSurtidoSugerido(models.Model):
    _inherit = 'sale.order'
    qou_sugerido = fields.Char(related='partner_id.sugerido',
                               string="Surtido Sugerido", readonly=True)


class PedidoPortal(models.Model):
    _inherit = 'sale.order'
    portal = fields.Char(string='Pedido Portal', size=6)


class Mostrador(models.Model):
    _inherit = 'sale.order'
    mostrador = fields.Boolean(default=False, string='Cliente Mostrador', )


class DetenerFactura(models.Model):
    _inherit = 'sale.order'
    dfactura = fields.Boolean(default=False, string='Detener Factura', )
