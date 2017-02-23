# -*- coding: utf-8 -*-

from openerp import models, fields

class Client(models.Model):

    _name = 'daigou.client'

    _rec_name = 'weixinname'

    name = fields.Char('姓名', required=True)

    weixinname = fields.Char('微信号')

    telephone = fields.Char('电话号码', required=True)

    adresse = fields.Char('地址', required=True)

    city = fields.Char('城市', required=True)

    cp = fields.Char('邮编')

    province = fields.Char('省份')

    country = fields.Char('国家')

    level_client = fields.Integer('客户等级')

    email_client = fields.Char('电子邮箱')
