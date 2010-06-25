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

# regexp completement gratuite pour l'instant.
def trim_extension(filename, extension):
    base = os.path.basename(filename)
    m = re.search (('(.*)\.%s' % extension), filename)
    return m.group(1)

def trim_extension2(filename):
    m = re.search ('(.*)\..*', filename)
    return m.group(1)

def make_test_id(path, number):
    base = os.path.basename(path)
    m = re.search ('(.*)\.svg', base)
    return "%s-%d" % (m.group(1), number)
    

# cree recursivement les repertoires mentionnes dans path
# sans lever d'erreur si ils existent deja
def mkdir_path(path):
    try:
        os.makedirs(path)
    except os.error, e:
        if e.errno != errno.EEXIST: raise