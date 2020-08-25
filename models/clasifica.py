# -*- coding: utf-8 -*-
from odoo import fields, models


class ClasificacionPartner(models.Model):
    _inherit = "res.partner"

    clasificaciones_ids = fields.Many2many(
        'marvelfields.clasificaciones', 'marvelfields_clasificaciones_rel',
        'src_id', 'dest_id',
        string='Clasificaciones')


class SubclasePartner(models.Model):
    _inherit = "res.partner"

    subclases_ids = fields.Many2many(
        'marvelfields.subclases', 'marvelfields_subclases_rel',
        'src_id', 'dest_id',
        string='Subclases')


class NoClientePartner(models.Model):
    _inherit = "res.partner"
    ncliente = fields.Char(string='Numero de Cliente', size=18)
