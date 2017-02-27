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


class DaigouOrder(models.Model):

    _name = 'daigou.order'

    _description = "orders"

    _order = 'date_order'

    date_order = fields.Date('Date for order', help="Date for the order item validation")

    client_id = fields.Integer('客户ID')

    order_item = fields.Char('商品名称')

    price_item_vente_unit_str = fields.Float('Price definition')

    price_item_vente_unit_fin = fields.Float('最终卖价')

    price_item_vente_unit_achat = fields.Float('商品购买价')

    qte_order = fields.Integer('下单数量')

    qte_ok = fields.Integer('已经购买数量')

    paye_total = fields.Float('付款总数')

    fl_baoyou = fields.Boolean('Active', help="是否包邮")

    fl_yunfei = fields.Boolean('Active', help="是否已经付运费")

    taux_achat = fields.Float('汇率')

    commentaire_achat = fields.Char('备注')

    #order_statut = fields.Selection([(0,u'已下单'), (1,u'采购完成'),(2,u'已经发货'),(99,u'退款')],u'订单状态')


