#!/usr/bin/python

import sys
from PyQt4.QtGui import QPixmap, QApplication
app = QApplication(sys.argv)
QPixmap.grabWindow(QApplication.desktop().winId()).save('test.png', 'png')
