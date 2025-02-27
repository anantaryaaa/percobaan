# -*- coding: utf-8 -*-
# from odoo import http


# class AssetHistory(http.Controller):
#     @http.route('/asset_history/asset_history', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/asset_history/asset_history/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('asset_history.listing', {
#             'root': '/asset_history/asset_history',
#             'objects': http.request.env['asset_history.asset_history'].search([]),
#         })

#     @http.route('/asset_history/asset_history/objects/<model("asset_history.asset_history"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('asset_history.object', {
#             'object': obj
#         })
