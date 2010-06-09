#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import rapport
import configuration
#from structure import Structure


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

def lancerPretraitements(tests):
    """Lance la serie des pretraitements tels que definis dans la stucture `tests'.
    On charge et execute en série les filtres, le nom du fichier résultat est dans
    le champ `output' de partie preprocessing de la structure `tests'."""
    # On prend chaque instance de chaque test.
    print '* Lancement des pretraitements.'
    for test in tests:
        for instance in test['execs']:
            preprocessing = instance['preprocessing']
            # Les fichiers resultats intermédiaires sont : source-Nb-module.svg
            source_filename = test['source']
            source_basename = util.trim_extension(source_filename, 'svg')

            filter_number = 0
            input_file = source_filename
            # TODO(m): regler le repertoire ou on sauve.
            preprocessing['filters'].insert(0, {'name' : 'identity',
                                                'parameters' : None })
            # Pour chaque filtre, on regle les fichiers
            # d'entrée/sortie, on charge le module python et on lance.
            for prefilter in preprocessing['filters']:
                output_file = '%s-%d-%s.svg' % (source_basename, filter_number,
                                                prefilter['name'])
                module = util.importer_module('pretraitement',
                                              prefilter['name'])
                module.go(input_file, output_file, prefilter['parameters'])

                filter_number = filter_number + 1
                input_file = output_file
            # Le fichier resultat est dans preprocessing['output']
            preprocessing['output'] = output_file

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
