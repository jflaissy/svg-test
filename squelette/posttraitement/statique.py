# -*- coding: utf-8 -*-

# un posttraitement prend une capture et la modifie
# travaille sur une image et en renvoie une autre

# les posttraitements peuvent etres chaines

# il met a jour la structure avec l'emplacement du fichier posttraite

# il doit y avoir un premier post-traitement bidon qui fait une copie de la capture
# et la reference dans le champ sortie du postT (si il n'y a pas de postT)

# un postt prend comme source le fichier de son champ sortie...
# c'est pas tres beau mais tant pis

# les posttraitements doivent archiver les anciens noms ?
# (l'automatiser hors du postT ?)

def go(s):
    print 'Postraitement statique.'
    s.posttraitement = True
