# -*- coding: utf-8 -*-
"""Module de capture par copie d'écran."""

import subprocess
import time
import sys
import os
import shutil
from PyQt4.QtGui import QPixmap, QApplication


def take_screenshot(filename):
    """Effectue une copie d'écran, stocke le résultat dans `filename'
    (auquel on ajoute l'extension)."""
    app = QApplication(sys.argv)
    format = 'bmp'
    output_file = filename + '.' + format
    QPixmap.grabWindow(QApplication.desktop().winId()).save(output_file, format)
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
    output_file = take_screenshot(output_prefix)
    p.kill()
    return output_file


#en PIL sous windows
#import ImageGrab
#img = ImageGrab.grab()
#img.save('test.jpg','JPEG')
