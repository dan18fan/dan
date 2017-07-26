# -*- encoding: utf-8 -*-

from odoo.report import report_sxw
from odoo.osv import osv

class reporte_ot(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(reporte_ot,self).__init__(cr,uid,name,context)

class reporte_ot_pdf(osv.AbstractModel)
    _name="report.orden_trabajo.orden_de_trabajo"
    _inherit="report.abstract_report"
    _template="orden_trabajo.orden_de_trabajo"
    _wrapped_report_class="reporte_ot"
