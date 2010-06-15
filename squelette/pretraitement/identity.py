# un pretraitement prend un fichier svg et en fait un autre il modifie
# le champ source de la structure.

# cf. remarques posttraitement/

import shutil

def go(input_file, output_file, parameters=None):
    print 'Pretraitement identite. in:', input_file, 'out:', output_file
    shutil.copyfile(input_file, output_file)
    
