# -*- coding: utf-8 -*-
# from odoo import http


# class Armushop(http.Controller):
#     @http.route('/armushop/armushop/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/armushop/armushop/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('armushop.listing', {
#             'root': '/armushop/armushop',
#             'objects': http.request.env['armushop.armushop'].search([]),
#         })

#     @http.route('/armushop/armushop/objects/<model("armushop.armushop"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('armushop.object', {
#             'object': obj
#         })
