# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SphMember(models.Model):
    _name='sph.member'
    _description="Member Registration"

    name = fields.Char(string='Name', required=True)
    # related_partner=fields.Many2one('res.partner', "Related Partner")
    date_of_joining=fields.Date(string='Date of joining')
    # category_id=fields.many2many('res.partner.category', string='Tags')
    city=fields.Char(string="City", required=True)
    street=fields.Char(string="Street", required=True)
    # country_id=fields.Many2one('res.country'string="Country" required=True)
    example = fields.Char(string='Example')
