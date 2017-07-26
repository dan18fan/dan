# -*- coding: utf-8 -*-
{
    'name': "Generador de Ordenes de Trabajo",
    'summary':"""
        Este módulo te permite crear una orden de trabajo de tus pedidos de ventas.""",
    'description': """
        Este módulo te permite crear una orden de trabajo de tus pedidos de ventas.""",
    'author': "Daniel Medina",
    'category': "",
    'version': '1.0',
    'depends': ['base','sale'],

    #Cargamos xmls
    'data': [
        "views/boton_ot.xml",
        "views/orden_trabajo_template.xml",
        "reports/orden_trabajo.xml",
    ],
    'installable': True,
    'auto_install': False,
}