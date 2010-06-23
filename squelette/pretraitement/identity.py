# -*- coding: utf-8 -*-

"""Prétraitement 'identité': ne modifie rien."""

import shutil



def go(input_file, output_file, parameters=None):
    print 'Pretraitement identite. in:', input_file, 'out:', output_file

    # Le fichier est sur le web, on le télécharge.
    if input_file[0:7] == 'http://':
        print 'ouech'
        import urllib
        print urllib.urlretrieve(input_file, output_file)
        print 'dans ', output_file
    else: # C'est un fichier normal, on copie.
        shutil.copyfile(input_file, output_file)
