# -*- coding: utf-8 -*-
from odoo import http

# class GestionEcole(http.Controller):
#     @http.route('/gestion_ecole/gestion_ecole/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_ecole/gestion_ecole/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_ecole.listing', {
#             'root': '/gestion_ecole/gestion_ecole',
#             'objects': http.request.env['gestion_ecole.gestion_ecole'].search([]),
#         })

#     @http.route('/gestion_ecole/gestion_ecole/objects/<model("gestion_ecole.gestion_ecole"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_ecole.object', {
#             'object': obj
#         })