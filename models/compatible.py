# -*- coding: utf-8 -*-

from odoo import models, fields


class Compatible (models.Model):
    _name = 'marvelfields.compatible'

    name = fields.Char(
        required=True,
        string='Compatible',
    )

    color = fields.Integer('Color Index', default=0)

    class CompatibleStock(models.Model):
        _inherit = "product.template"

        compatible_ids = fields.Many2many(
            'marvelfields.compatible', 'marvelfields_compatible_rel',
            'src_id', 'dest_id',
            string='Compatibles')
