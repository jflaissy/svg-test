#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-
"""Fichier principal du programme. Lance les opérations sur l'ensemble
de la chaine de tests, depuis la lecture du fichier XML de
configuration à l'export du rapport généré."""

import util
import os
import sys
import parser_xml
import report
from xml.sax import parse

#from structure import Structure


conf = { }

def go(config_file):
    """Pilote toute la chaine de tests."""
    init()
    parser_Config=parser_xml.Parser()
    #On parse
    parse(config_file, parser_Config)
    #On verifie que la methode nous renvoi bien la structure apres parsage
    tests = parser_Config.getStructure()
    print 'TTTTTTTTTTTTTTT'
    print tests

    # Idée: on passe a travers un module de preT, capture, un mod. de postT,
    # un mod. de diag, puis on genere le rapport
    initalizeTests(tests)
    launchPreprocessing(tests)
    launchCapture(tests)
    launchPostprocessing(tests)
    launchDiagnostic(tests)

    #rapport.go(tests)
    launchReport(tests)
    #print tests

def initalizeTests(tests):
    """Initalise la structure de tests pour faciliter l'utilisation
    après. Création d'identifiants uniques pour les filtres, les tests
    etc."""
    test_nb = 1
    for test in tests:
        test['test_id'] = util.make_test_id(test['source'], test_nb)
        #print test['test_id']
        instance_nb = 1
        for instance in test['execs']:
            instance['instance_id'] = "%d_%s" % (instance_nb, instance['browser'])
            instance_nb = instance_nb + 1
            filter_nb = 1
            for prefilter in instance['preprocessing']['filters']:
                prefilter['filter_id'] = filter_nb
                filter_nb = filter_nb + 1
            filter_nb = 1
            for postfilter in instance['postprocessing']['filters']:
                postfilter['filter_id'] = filter_nb
                filter_nb = filter_nb + 1
            print 'BBBBBBBBBBBOUM!'
            print instance['capture']
            instance['capture']['parameters']['browser'] = instance['browser']
        test_nb = test_nb + 1

##
# Lanceurs.
def launchPreprocessing(tests):
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
            input_file = source_filename
            preprocessing['filters'].insert(0, {'name' : 'identity',
                                                'filter_id' : 0,
                                                'parameters' : None })
            # Pour chaque filtre, on regle les fichiers
            # d'entrée/sortie, on charge le module python et on lance.
            for prefilter in preprocessing['filters']:
                output_filename = '%s-%s-%s-%s.svg' % (test['test_id'],
                                                       instance['instance_id'],
                                                       prefilter['filter_id'],
                                                       prefilter['name'])
                output_file = os.path.join(conf['preprocessing_directory'], output_filename)

                module = util.importer_module('pretraitement',
                                              prefilter['name'])
                module.go(input_file, output_file, prefilter['parameters'])
                input_file = output_file
            # Le fichier resultat est dans preprocessing['output']
            preprocessing['output'] = output_file

def launchCapture(tests):
    """Lance les captures. `tests' est la grande structure de tests.
    Le résultat de chaque capture est stocké dans capture['output']"""
    print '* Lancement des captures.'
    for test in tests:
        for instance in test['execs']:
            capture = instance['capture']
            module_nom = capture['name']
            module = util.importer_module('capture', module_nom)
            source_filename = test['source']
            output_filename = '%s-%s-%s' % (test['test_id'],
                                            instance['instance_id'],
                                            capture['name'])
            input_file = instance['preprocessing']['output']
            output_prefix = os.path.join(conf['capture_directory'], output_filename)
            output_file = module.go(input_file, output_prefix,
                                    capture['parameters'])
            capture['output'] = output_file

def launchPostprocessing(tests):
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

            input_file = instance['capture']['output']
            postprocessing['filters'].insert(0, {'name' : 'identity',
                                                 'filter_id' : 0,
                                                'parameters' : None })
            # Pour chaque filtre, on regle les fichiers
            # d'entrée/sortie, on charge le module python et on lance.
            for postfilter in postprocessing['filters']:
                output_filename = '%s-%s-%s-%s' % (test['test_id'],
                                                       instance['instance_id'],
                                                       postfilter['filter_id'],
                                                       postfilter['name'])
                output_prefix = os.path.join(conf['postprocessing_directory'],
                                             output_filename)

                module = util.importer_module('posttraitement',
                                              postfilter['name'])
                output_file = module.go(input_file, output_prefix,
                                        postfilter['parameters'])
                input_file = output_file
            # Le fichier resultat est dans postprocessing['output']
            postprocessing['output'] = output_file

def buildComparisons(tests):
    """Pour chaque test, construit les instances de comparaisons, en
    croisant les résultats si plusieurs navigateurs ont été lancés par
    exemple. On met à jour les test['comparison']."""
    for test in tests:
        comparisons = [ ]
        # type separé, on crée une comparaison par instance d'execution
        if test['type'] == 'separate':
            for instance in test['execs']:
                comp = { 'instances': [ instance ] }
                comparisons.append(comp)
                comp['comparison_id'] = instance['instance_id']
        else:
            assert test['type'] == 'compare'
            for instance1 in test['execs']:
                for instance2 in test['execs']:
                    if instance1 == instance2:
                        continue
                    comp = { 'instances': [ instance1, instance2 ] }
                    comp['comparison_id'] = instance1['instance_id'] \
                        + '_' + instance2['instance_id']
                    comparisons.append(comp)
        test['comparisons'] = comparisons

def launchDiagnostic(tests):
    """Lance les diagnostics. `tests' est la grande structure de
    tests.  Pour chaque comparaison, on lance le module de diagnostic
    défini dans la structure."""
    print '* Lancement des captures.'
    buildComparisons(tests)
    for test in tests:
        for comparison in test['comparisons']:

            diagnostic = test['diagnostic']
            module_nom = diagnostic['name']
            module = util.importer_module('diagnostic', module_nom)
            source_filename = test['source']
#            source_basename = util.trim_extension(source_filename, 'svg')

            output_prefix = os.path.join(conf['capture_directory'], comparison['comparison_id'] )
            #module.go(comparison, output_prefix, diagnostic['parameters'])
            module.go(comparison, output_prefix, diagnostic)

def launchReport(tests):
    """Lance le générateur de rapport."""
    print '* Lancement du rapport.'
    output_file = os.path.join(conf['report_directory'], 'report.xml')
    report.go(tests, output_file)

def init():
    """Initialise la configuration du programme. En particulier, on
    règle les repertoires où seront sauvés les résultats
    intermédiaires."""
    # verifie la version
    # besoin de 2.6 pour le kill de processus
    if sys.version_info < (2,6):
        print 'You need python >= 2.6 to run this program.'
        sys.exit(2)

    global conf
    pid = os.getpid()
    # creation des repertoires de stockage des fichiers temporaires
    working_directory =  os.path.join('results', '%s' % pid)
    conf['working_directory'] = working_directory
    conf['preprocessing_directory'] = os.path.join(working_directory, 'preprocessing')
    conf['capture_directory'] = os.path.join(working_directory, 'capture')
    conf['postprocessing_directory'] = os.path.join(working_directory, 'postprocessing')
    conf['diagnostic_directory'] = os.path.join(working_directory, 'diagnostic')
    conf['report_directory'] = os.path.join(working_directory, 'report')
    util.mkdir_path(working_directory)
    for directory in conf.values():
        util.mkdir_path(directory)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        go(sys.argv[1])
    else:
        print 'Usage: %s <fichier.xml>' % sys.argv[0]
        print '\toù <fichier.xml> est le fichier de configuration des tests.'
