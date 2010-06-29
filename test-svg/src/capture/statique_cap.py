# -*- coding: utf-8 -*-
"""Module de capture par copie d'écran."""

import subprocess
import time
import sys
import os
import shutil
import platform
import threading
import signal

need_sleep = False # pour la gestion des sleep()

def screenshot_qt4(filename):
    """Effectue une copie d'écran, stocke le résultat dans `filename'
    (auquel on ajoute l'extension)."""
    from PyQt4.QtGui import QPixmap, QApplication
    app = QApplication(sys.argv)
    format = 'bmp'
    output_file = filename + '.' + format
    QPixmap.grabWindow(QApplication.desktop().winId()).save(output_file, format)
    return output_file

def screenshot_mac(filename):
    """Effectue une copie d'écran, stocke le résultat dans `filename'
    (auquel on ajoute l'extension)."""
    import subprocess
    format = 'bmp'
    output_file = filename + '.' + format
    p = subprocess.Popen(['screencapture', '-t', format, output_file])
    time.sleep(5)
    return output_file

def screenshot_pil(filename):
    """Effectue une copie d'écran sous Windows, avec la librairie PIL."""
    import ImageGrab
    format = 'bmp'
    output_file = filename + '.' + format
    img = ImageGrab.grab()
    img.save(output_file, format)
    return output_file

def setup_file(filename, parameters):
    """Met en place la page HTML (faisant référence au SVG) qui sera
    chargé par le navigateur."""
    cap_dir = os.path.join(os.getcwd(), 'capture',
                             'statique-cap-files')
    file_path = os.path.join('..', '..', filename)
    page_path = os.path.join(cap_dir, 'page.html')
    dest = open(page_path, 'w')
    header = os.path.join(cap_dir, 'page-header')
    footer = os.path.join(cap_dir, 'page-footer')
    headfile = open(header, 'r')
    footfile = open(footer, 'r')
    dest.write(headfile.read())
    # Ecriture des parametres dynamiques : nom de fichier, taille.
    dest.write('src=\"' + file_path + "\" height=\"" + parameters['height']
               + "\" width=\"" + parameters['width'] + "\"")
    dest.write(footfile.read())
    dest.close()
    headfile.close()
    footfile.close()

def set_platform():
    """Trouve la plateforme sous laquelle tourne le programme
    (Linux/Windows/Mac)."""
    syst = platform.system()
    plat_linux, plat_win, plat_mac= False, False, False
    if syst == 'Linux':
        plat_linux = True
    elif syst == 'Windows':
        plat_win = True
    elif syst == 'Darwin':
        plat_mac = True
    return (plat_linux, plat_mac, plat_mac)

def go(input_file, output_prefix, parameters):
    global need_sleep
    print 'capture statique ' , parameters['browser'], 'in:', input_file, 'out:', output_prefix

    plat_linux, plat_mac, plat_mac = set_platform()

    page_path = os.path.join(os.getcwd(), 'capture',
                             'statique-cap-files', 'page.html')
    setup_file(input_file, parameters)
    # le lanceur de navigateur (cf. classe ci dessous)
    launcher = BrowserLauncher([parameters['browser'], page_path])
    launcher.start()
    print 'Sleep 10s...'
    # on accroche un gestionnaire du signal 17 pour gérer le conflit
    # entre le sleep et le processus fils qui fait remonter des signaux.
    need_sleep = True
    if plat_linux:
        signal.signal(17, sighandler)
    time.sleep(10)
    p = launcher.finish()
    need_sleep = False
    # screenshot different selon la plateforme
    if plat_linux:
        output_file = screenshot_qt4(output_prefix)
    elif plat_win:
        output_file = screenshot_pil(output_prefix)
    elif plat_mac:
        output_file = screenshot_mac(output_prefix)

    p.kill()
    return output_file

def sighandler(signum, stackframe):
    """Un gestionnaire de signaux qui gère les périodes de sommeil,
    pérturbées par le fork() et les signaux 17 qui remontent."""
    global need_sleep
    if need_sleep:
        time.sleep(10)

class BrowserLauncher(threading.Thread):
    """Lance un navigateur dans un nouveau thread, pour résoudre des problèmes de signaux.
    `command_line' est la commande à lancer, un tableau d'arguments."""
    def __init__(self, command_line):
        threading.Thread.__init__(self)
        self.p = None
        self.command_line = command_line
    def run(self):
        self.p = subprocess.Popen(self.command_line)
    def finish(self):
        return self.p

