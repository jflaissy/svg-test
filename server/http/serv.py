#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# serv.py - Serveur web ultra basique qui intercepte les GET
# pour pouvoir les gérer à la main.

import SimpleHTTPServer, BaseHTTPServer

class InterceptGETHandler (SimpleHTTPServer.SimpleHTTPRequestHandler):
    """Handler pour rajouter un comportement specifique au GET."""

    def do_GET (self):
        """Override la gestion du GET."""
	print 'Interception du GET.'
        # fait gerer la requete par le module
	SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def run(server_class = BaseHTTPServer.HTTPServer,
        handler_class = BaseHTTPServer.BaseHTTPRequestHandler):
    """Lancer un serveur web."""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


# on cree un serveur, un handler customisé et on lance le serveur
handler = InterceptGETHandler
server = BaseHTTPServer.HTTPServer
run(server, handler)
