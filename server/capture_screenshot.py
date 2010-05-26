#!/usr/bin/python

import sys
from PyQt4.QtGui import QPixmap, QApplication

window_id = 0

def init():
    global window_id
    app = QApplication(sys.argv)
    window_id = QApplication.desktop().winId()

def take_screenshot(filename):
    QPixmap.grabWindow(window_id).save(filename + '.png', 'png')
