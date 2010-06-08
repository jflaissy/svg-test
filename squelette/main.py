#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import rapport
import configuration
from structure import Structure


def go():
    print 'Main.'
    # on recupere la structure
    strct = configuration.lire_configuration()

    # Idée: on passe a travers un module de preT, capture, un mod. de postT,
    # un mod. de diag, puis on genere le rapport
    lancerPretraitements(strct)
    lancerCaptures(strct)
    lancerPosttraitements(strct)
    lancerDiagnostics(strct)

    rapport.go(strct)

##
# Lanceurs.

def lancerPretraitements(struct):
    # Code bidon: pour chaque test de la structure
    # pour chaque exec
    for i in [1]:
        # initaliser le preT (copier le nom de source .svg)
        # pour chaque module de preT : charger/lancer
        for j in [1]:
            module_type = 'pretraitement'
            module_nom = 'vide'
            module = util.importer_module(module_type, module_nom)
            module.go(struct)

def lancerCaptures(struct):
    # Code bidon: pour chaque test de la structure
    # pour chaque exec
    for i in [1]:
        module_nom = 'statique' # lire module_nom dans la structure
        module_type = 'capture'
        module = util.importer_module(module_type, module_nom)
        module.go(struct)

def lancerPosttraitements(struct):
    # Code bidon: pour chaque test de la structure
    # pour chaque exec
    for i in [1]:
        # initaliser le postT (copier le nom de la sortie capture dans
        # sortie postT)
        # pour chaque module de postT : charger/lancer
        for j in [1]:
            module_type = 'posttraitement'
            module_nom = 'statique'
            module = util.importer_module(module_type, module_nom)
            module.go(struct)

def lancerDiagnostics(struct):
    # construire les structures comparaisons, referencer les execs
    # Code bidon: pour chaque test de la structure
    # pour chaque comparaison
    for i in [1]:
        module_type = 'diagnostic'
        module_nom = 'histogramme'
        module = util.importer_module(module_type, module_nom)
        module.go(struct)


if __name__ == '__main__':
    go()
