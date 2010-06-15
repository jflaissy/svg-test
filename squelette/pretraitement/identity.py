# -*- coding: utf-8 -*-

"""Prétraitement 'identité': ne modifie rien."""

import shutil

def go(input_file, output_file, parameters=None):
    print 'Pretraitement identite. in:', input_file, 'out:', output_file
    shutil.copyfile(input_file, output_file)
    
