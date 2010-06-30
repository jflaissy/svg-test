# -*- coding: utf-8 -*-
"""Prétraitement 'identité': ne modifie rien. Télécharge le fichier
sur le web si il y a besoin."""

import shutil

def go(input_file, output_file, parameters=None):
    print 'Pretraitement identite. in:', input_file, 'out:', output_file
    # Le fichier est sur le web, on le télécharge.
    if input_file[0:7] == 'http://':
        import urllib
        urllib.urlretrieve(input_file, output_file)
    else: # C'est un fichier normal, on copie.
        shutil.copyfile(input_file, output_file)
