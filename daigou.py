# -*- coding: utf-8 -*-

from openerp import models, fields, api

#----------------------------------------------------------
# Clients
#----------------------------------------------------------
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

#----------------------------------------------------------
# Categories
#----------------------------------------------------------
class ProductCategory(models.Model):

    _name = 'daigou.product.category'

    _description = "Product Category"

    _rec_name = 'name'

    name = fields.Char('产品类别名称', required=True)

    complete_name = fields.Char('产品类别描述', required=True)

    parent_id = fields.Many2one('daigou.product.category','Parent Category', select=True, ondelete='cascade')

    child_id = fields.One2many('daigou.product.category', 'parent_id', string='Child Categories')

    sequence = fields.Integer('Sequence', select=True, help="Gives the sequence order when displaying a list of product categories.")

    type = fields.Selection([('view','View'), ('normal','Normal')], 'Category Type', help="A category of the view type is a virtual category that can be used as the parent of another category to create a hierarchical structure.")


