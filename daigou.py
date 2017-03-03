# -*- coding: utf-8 -*-

from datetime import date
from openerp import models, fields, api

#----------------------------------------------------------
# Clients
#----------------------------------------------------------
class Client(models.Model):

    _name = 'daigou.client'
    _description = "Clients for daigou"
    _rec_name = 'weixin_id'

    def show_client_order_form_view(self, cr, uid, ids, context=None):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'daigou.order',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new',
        }

    name = fields.Char(u'姓名', required=True)
    weixin_id = fields.Char(u'微信号')
    telephone = fields.Char(u'电话号码', required=True)
    adresse = fields.Char(u'地址', required=True)
    city = fields.Char(u'城市', required=True)
    cp = fields.Char(u'邮编')
    province = fields.Char(u'省份')
    country = fields.Char(u'国家')
    level_client = fields.Integer(u'客户等级')
    email_client = fields.Char(u'电子邮箱')

#----------------------------------------------------------
# Categories
#----------------------------------------------------------
class ProductCategory(models.Model):

    _name = 'daigou.product.category'
    _description = "Product Category"
    _rec_name = 'name'

    name = fields.Char(u'产品类别名称', required=True)
    complete_name = fields.Char(u'产品类别描述', required=True)
    parent_id = fields.Many2one('daigou.product.category','Parent Category', select=True, ondelete='cascade')
    child_id = fields.One2many('daigou.product.category', 'parent_id', string='Child Categories')
    sequence = fields.Integer('Sequence', select=True, help="Gives the sequence order when displaying a list of product categories.")
    type = fields.Selection([('view','View'), ('normal','Normal')], 'Category Type', help="A category of the view type is a virtual category that can be used as the parent of another category to create a hierarchical structure.")

#----------------------------------------------------------
# Orders : every order for one client
#----------------------------------------------------------
class DaigouOrder(models.Model):

    _name = 'daigou.order'
    _description = "orders"
    _order = 'date_order desc, weixin_id'

    date_order = fields.Date('下单日期', help="下单日期缺省是当天日期",default=date.today().strftime('%Y-%m-%d'))
    weixin_id = fields.Many2one('daigou.client', required=True, index=True)
    order_item = fields.Char(u'商品名称')
    price_item_vente_unit_str = fields.Float(u'商品最初定价')
    price_item_vente_unit_fin = fields.Float(u'最终卖价')
    price_item_vente_unit_achat = fields.Float(u'商品购买价')
    qte_order = fields.Integer(u'下单数量',default=1)
    qte_ok = fields.Integer(u'已经购买数量')
    paye_total = fields.Float(u'付款总数')
    fl_baoyou = fields.Boolean(u'是否包邮')
    fl_yunfei = fields.Boolean(u'运费是否已付')
    price_liv = fields.Float(u'国内已付运费')
    taux_achat = fields.Float(u'汇率')
    commentaire_achat = fields.Text(u'订单备注')
    #weixinname = fields.Char('Weixin ID', related='daigou.client.weixinname', store=True)
    order_statut = fields.Selection([('0',u'已下单'), ('1',u'采购完成'),('2',u'已经发货'),('3',u'已结算'),('99',u'退款')], readonly=True, index=True, default='0')


