# -*- coding: utf-8 -*-
"""Module de capture par copie d'écran."""

import subprocess
import time
import sys
import os
from PyQt4.QtGui import QPixmap, QApplication

def take_screenshot(filename):
    """Effectue une copie d'écran, stocke le résultat dans `filename'
    (auquel on ajoute l'extension)."""
    app = QApplication(sys.argv)
    format = 'bmp'
    output_file = filename + '.' + format
    QPixmap.grabWindow(QApplication.desktop().winId()).save(output_file, format)
    return output_file
    
def go(input_file, output_prefix, parameters):
    print 'Capture statique ' , parameters['browser'], 'in:', input_file, 'out:', output_prefix
    page_path = os.path.join(os.getcwd(), 'capture',
                             'statique-cap-files', 'page.html')
    p = subprocess.Popen([parameters['browser'], page_path])
    print 'sleep 10s...'
    time.sleep(10)
    print 'ok'
    output_file = take_screenshot(output_prefix)
    p.kill()
    return output_file


#import ImageGrab
#img = ImageGrab.grab()
#img.save('test.jpg','JPEG')
