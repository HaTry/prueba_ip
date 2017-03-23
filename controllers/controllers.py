# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class pruebaIp(http.Controller):
    @http.route('/prueba_ip/', type='http', auth='public', website=True)
    def prueba_ip(self, **kw):
        ip = request.httprequest.environ['REMOTE_ADDR']
        return "Mi IP es: " + str(ip)