#!/usr/bin/env python

import util
import rapport
import configuration
from structure import Structure

def go():
    print 'Main.'
    # on recupere la structure
    strct = configuration.lire_configuration()

    # Idée: on passe a travers un module de capture, un mod. de preT,
    # un mod. de diag, puis on genere le rapport

    # Code bidon: pour chaque test de la structure
    for i in [1]:
        module_nom = 'statique' # lire module_nom dans la structure
        module_type = 'capture'
        module = util.importer_module(module_type, module_nom)
        module.go(strct)

    # Code bidon: pour chaque test de la structure
    for i in [1]:
        module_type = 'pretraitement'
        module_nom = 'statique'
        module = util.importer_module(module_type, module_nom)
        module.go(strct)

    # Code bidon: pour chaque test de la structure
    for i in [1]:
        module_type = 'diagnostic'
        module_nom = 'histogramme'
        module = util.importer_module(module_type, module_nom)
        module.go(strct)

    rapport.go(strct)

if __name__ == '__main__':
    go()
