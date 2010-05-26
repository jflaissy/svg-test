#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# httpd_server.py - Serveur web ultra basique qui intercepte les GET
# pour pouvoir les gérer à la main.

import SimpleHTTPServer, BaseHTTPServer
import time
import os
#from ..capture import screenshot
#from .. import capture
#from .. import capture.screenshot
#import screenshot
import capture_screenshot

class InterceptGETHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """Handler pour rajouter un comportement specifique au GET."""

    def do_GET(self):
        """Override la gestion du GET. Lance un screenshot avant
        chargement."""
	print 'Interception du GET.'
        print 'Capture en cours.'
        time.sleep(1) # temporaire : on dort avant de lancer la capture
        capture_screenshot.take_screenshot('sshot'
                                           + self.path.replace('/', '-'))
        print 'Capture terminée.'
	SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

def run_server():
    """Lancer le serveur web."""
    # on cree un serveur, un handler customisé et on lance le serveur
    handler = InterceptGETHandler
    server = BaseHTTPServer.HTTPServer
    server_address = ('', 8080)
    httpd = server(server_address, handler)
    httpd.serve_forever()

def set_environment():
    """Se place dans le bon répertoire."""
    os.chdir('pages/')

def run():
    """Fonction principale. Met en place l'environnement et lance le serveur."""
    set_environment()
    run_server()
