# Fonctions utilitaires diverses utilisees ailleurs dans le code.

def importer_module(module_type, module_nom):
    """Importe un module.
    module_type est 'capture', 'pretraitement' ou 'diagnostic'
    module_nom est le nom du module dans ce repertoire."""
    module = __import__('%s.%s' % (module_type, module_nom),
                        fromlist=[module_type])
    return module
