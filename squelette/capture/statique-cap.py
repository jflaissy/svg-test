# -*- coding: utf-8 -*-
"""Module de capture par copie d'écran."""

import subprocess
import time
import sys
import os
import shutil
import platform
from PyQt4.QtGui import QPixmap, QApplication

def screenshot_qt4(filename):
    """Effectue une copie d'écran, stocke le résultat dans `filename'
    (auquel on ajoute l'extension)."""
    print 'cap linux'
    from PyQt4.QtGui import QPixmap, QApplication
    app = QApplication(sys.argv)
    format = 'bmp'
    output_file = filename + '.' + format
    QPixmap.grabWindow(QApplication.desktop().winId()).save(output_file, format)
    return output_file

def screenshot_mac(filename):
    """Effectue une copie d'écran, stocke le résultat dans `filename'
    (auquel on ajoute l'extension)."""
    print 'cap mac'
    import subprocess
    format = 'bmp'
    output_file = filename + '.' + format
    p = subprocess.Popen(['screencapture', '-t', format, output_file])
    return output_file

def screenshot_pil(filename):
    """Effectue une copie d'écran sous Windows, avec la librairie PIL."""
    print 'cap win'
    import ImageGrab
    format = 'bmp'
    output_file = filename + '.' + format
    img = ImageGrab.grab()
    img.save(output_file, format)
    return output_file

def setup_file(filename):
    """Met en place le fichier SVG qui sera chargé par le navigateur."""
    file_path = os.path.join(os.getcwd(), 'capture',
                             'statique-cap-files', 'file.svg')

    shutil.copyfile(filename, file_path)

def go(input_file, output_prefix, parameters):
    print 'Capture statique ' , parameters['browser'], 'in:', input_file, 'out:', output_prefix
    page_path = os.path.join(os.getcwd(), 'capture',
                             'statique-cap-files', 'page.html')
    setup_file(input_file)
    p = subprocess.Popen([parameters['browser'], page_path])
    print '\t\tSleep 10s...',
    time.sleep(10)
    print 'ok.'

    syst = platform.system()
    if syst == 'Linux':
        output_file = screenshot_qt4(output_prefix)
    elif syst == 'Windows':
        output_file = screenshot_pil(output_prefix)
    elif syst == 'Darwin':
        output_file = screenshot_mac(output_prefix)

    p.kill()
    return output_file
