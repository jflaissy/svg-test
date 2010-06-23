###
# -*- coding: utf-8 -*-
"""Prétraitement qui enleve le texte du fichier svg"""

import subprocess

def go(input_file, output_file, parameters=None):
     p = subprocess.Popen(['xsltproc', '-o', output_file,'svg_filter_text.xsl', input_file])
##
