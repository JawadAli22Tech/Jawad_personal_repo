# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class StockPicking(models.Model):
    _inherit = "stock.picking"
    def state_to_draft(self):
        for rec in self:
            if rec.state:
                rec.state = 'draft'
            else:
                None
    def action_cancel(self):
        for rec in self:
            if rec.state:
                rec.state = 'cancel'
            else:
                None
    # def state_to_draft(self):
    #     picking_id = 38
    #     picking = self.browse(picking_id)
    #     if picking:
    #         picking.unlink()
    #     else:
    #         None
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    def button_cancel(self):
        for rec in self:
            if rec.state:
                rec.state = 'cancel'
            else:
                None


