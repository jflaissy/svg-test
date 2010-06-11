#!/usr/bin/env python
# -*- coding: utf-8 -*-

import util
import rapport
import configuration
import os
import parser
from xml.sax import parse

#from structure import Structure


conf = { }

def go():
    parser_Config=parser.Parser()
    #On parse
    parse('example.xml', parser_Config)
    #On verifie que la methode nous renvoi bien la structure apres parsage
    strct =parser_Config.getStructure()
    #print strct

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
            # TODO(m): on fait ca plusieurs fois
            # TODO(m): espaces dans les noms de fichiers
            preprocessing['filters'].insert(0, {'name' : 'identity',
                                                'parameters' : None })
            # Pour chaque filtre, on regle les fichiers
            # d'entrée/sortie, on charge le module python et on lance.
            for prefilter in preprocessing['filters']:
                output_filename = '%s-%d-%s.svg' % (source_basename,
                                                   filter_number,
                                                   prefilter['name'])
                output_file = os.path.join(conf['preprocessing_directory'], output_filename)

                module = util.importer_module('pretraitement',
                                              prefilter['name'])
                module.go(input_file, output_file, prefilter['parameters'])

                filter_number = filter_number + 1
                input_file = output_file
            # Le fichier resultat est dans preprocessing['output']
            preprocessing['output'] = output_file

def lancerCaptures(tests):
    """Lance les captures. `tests' est la grande structure de tests.
    Le résultat de chaque capture est stocké dans capture['output']"""
    print '* Lancement des captures.'
    for test in tests:
        for instance in test['execs']:
            capture = instance['capture']
            module_nom = capture['name']
            module = util.importer_module('capture', module_nom)
            source_filename = test['source']
            source_basename = util.trim_extension(source_filename, 'svg')
            input_file = instance['preprocessing']['output']
            output_prefix = os.path.join(conf['capture_directory'], source_basename)
            output_file = module.go(input_file, output_prefix,
                                    capture['parameters'])
            capture['output'] = output_file

def lancerPosttraitements(tests):
    """Lance la serie des posttraitements tels que definis dans la stucture `tests'.
    On charge et execute en série les filtres, le nom du fichier résultat est dans
    le champ `output' de partie preprocessing de la structure `tests'."""
    # On prend chaque instance de chaque test.
    print '* Lancement des posttraitements.'
    for test in tests:
        for instance in test['execs']:
            postprocessing = instance['postprocessing']
            # Les fichiers resultats intermédiaires sont
            source_filename = test['source']
            source_basename = util.trim_extension(source_filename, 'svg')
            input_file = source_filename
            filter_number = 0
            postprocessing['filters'].insert(0, {'name' : 'identity',
                                                'parameters' : None })
            # Pour chaque filtre, on regle les fichiers
            # d'entrée/sortie, on charge le module python et on lance.
            for postfilter in postprocessing['filters']:
                output_filename = '%s-%d-%s' % (source_basename,
                                                   filter_number,
                                                   postfilter['name'])
                output_prefix = os.path.join(conf['postprocessing_directory'], output_filename)

                module = util.importer_module('posttraitement',
                                              postfilter['name'])
                output_file = module.go(input_file, output_prefix,
                                        postfilter['parameters'])
                filter_number = filter_number + 1
                input_file = output_file
            # Le fichier resultat est dans postprocessing['output']
            postprocessing['output'] = output_file

# TODO
# devrait ressembler à capture
def lancerDiagnostics(struct):
    # construire les structures comparaisons, referencer les execs
    # Code bidon: pour chaque test de la structure
    # pour chaque comparaison
    for i in [1]:
        module_type = 'diagnostic'
        module_nom = 'histogramme'
        module = util.importer_module(module_type, module_nom)
        module.go(struct)

def init():
    """Initialise la configuration du programme. En particulier, on
    règle les repertoires où seront sauvés les résultats
    intermédiaires."""
    global conf
    pid = os.getpid()
    working_directory =  os.path.join('results', '%s' % pid)
    util.mkdir_path(working_directory)
    conf['working_directory'] = working_directory
    conf['preprocessing_directory'] = os.path.join(working_directory, 'preprocessing')
    conf['capture_directory'] = os.path.join(working_directory, 'capture')
    conf['postprocessing_directory'] = os.path.join(working_directory, 'postprocessing')
    conf['report_directory'] = os.path.join(working_directory, 'report')

if __name__ == '__main__':
    init()
    go()
