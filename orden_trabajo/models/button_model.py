# -*- coding: utf-8 -*-
from odoo import models, api

class boton_orden_trabajo(models.Model):
    _inherit = 'sale.order'
    _name = 'boton.ot'


    @api.multi
    def print_work_order(self):
        return self.env['report'].get_action(self, 'orden_trabajo.orden_de_trabajo')