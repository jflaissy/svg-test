# Fonctions utilitaires diverses utilisees ailleurs dans le code.

import re

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
    m = re.search (('(.*)\.%s' % extension), filename)
    return m.group(1)
