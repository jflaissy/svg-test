# un pretraitement prend un fichier svg et en fait un autre il modifie
# le champ source de la structure.

# cf. remarques posttraitement/


def go(input_file, output_prefix, parameters=None):
    print 'Posttraitement identite. in:', input_file, 'out:', output_prefix
    output_file = "%s.png" % output_prefix
    return output_file
