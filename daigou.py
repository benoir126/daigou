# -*- coding: utf-8 -*-

from openerp import models, fields

class Client(models.Model):

    _name = 'daigou.client'

    _rec_name = 'weixinname'

    name = fields.Char('Name', required=True)

    weixinname = fields.Char('Wei Xin ID')  

    telephone = fields.Char('number of telephone', required=True)

    adresse = fields.Char('adresse of client', required=True)

    city = fields.Char('The city', required=True)

    cp = fields.Char('Code postal')

    province = fields.Char('The province')

    country = fields.Char('The country')

    level_client = fields.Integer('User level')

    email_client = fields.Char('The Email')
