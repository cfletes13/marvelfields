# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SurtidoSugerido (models.Model):
	_inherit = 'res.partner'

	sugerido = fields.Char(string='Surtido Sugerido',)
	warehouse_sugerido_id = fields.Many2one('stock.warehouse',string="Surtido Sugerido", help="Almacen sugerido del cual se ba a surtir el pedido del cliente")


class RutaVendedor (models.Model):
	_inherit = 'res.partner'

	rutav = fields.Char(string='Ruta',)


class SaleOrderFields(models.Model):
	_inherit = 'sale.order'

	qou_sugerido = fields.Char(related='partner_id.sugerido',string="Surtido Sugerido", readonly=True)
	portal = fields.Char(string='Pedido Portal', size=15)
	mostrador = fields.Boolean(default=False, string='Cliente Mostrador', )
	dfactura = fields.Boolean(default=False, string='Detener Factura', )

	@api.onchange('partner_id')
	def onchange_warehouse_partner_id(self):
		if not self.partner_id:
			return

		self.update({'warehouse_id': self.partner_id.warehouse_sugerido_id.id})

class SugeridoWarehouse(models.Model):
	_inherit = 'stock.warehouse'
	sugerido = fields.Char(string='Surtido Sugerido',)