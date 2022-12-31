# -*- coding: utf-8 -*-

from odoo import fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    limite_credito = fields.Integer(string="Limite de crédito")