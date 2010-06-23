###
# -*- coding: utf-8 -*-
"""Prétraitement qui enleve le texte du fichier svg."""

import subprocess
import os

def go(input_file, output_file, parameters=None):
     # On lance le programme xsltproc sur la feuille de style dans xslt/.
     xsl_path = os.path.join('xslt', 'svg_filter_text.xsl')
     p = subprocess.Popen(['xsltproc', '-o', output_file, xsl_path, input_file])
