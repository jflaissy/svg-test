# -*- coding: utf-8 -*-
"""Fonctions utilitaires diverses utilisees ailleurs dans le code."""

import re
import os
import errno

def importer_module(module_type, module_nom):
    """Importe un module.
    module_type est 'capture', 'pretraitement' ou 'diagnostic'
    module_nom est le nom du module dans ce repertoire."""
    print '\t\t\t\t\t[d] Import de %s/%s' % (module_type, module_nom)
    module = __import__('%s.%s' % (module_type, module_nom),
                        fromlist=[module_type])
    return module

def make_test_id(path, number):
    """Construit l'id d'un test à partir du chemin du fichier."""
    base = os.path.basename(path)
    m = re.search ('(.*)\.svg', base)
    return "%s-%d" % (m.group(1), number)

def mkdir_path(path):
    """Crée recursivement les repertoires mentionnes dans path
    sans lever d'erreur si ils existent deja"""
    try:
        os.makedirs(path)
    except os.error, e:
        if e.errno != errno.EEXIST: raise
