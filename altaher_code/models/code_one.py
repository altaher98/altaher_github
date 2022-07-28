# -*- coding: utf-8 -*-

from odoo import models, fields, api


class editCode(models.Model):

    _name = "code.edit"

    name = fields.Char(string='Name', required=True)
    number = fields.Float(string='Number',required=True)