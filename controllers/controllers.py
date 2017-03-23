# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class pruebaIp(http.Controller):
    @http.route('/prueba_ip/', type='http', auth='public', website=True)
    def prueba_ip(self, **kw):
        ip = request.httprequest.remote_addr
        ip_real = request.httprequest.environ['HTTP_X_REAL_IP']
        return "Mi IP es: " + str(ip) + " <br> Mi IP real: " + ip_real