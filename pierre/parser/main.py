#Partie ou on parse notre fichier xml
import ../parser
from xml.sax import parse

#Partie ou on parse notre fichier xml

parser_Config=parser.Parser()
#On verifie qu'on ne peut pas avoir la structure sans parser le xml!
#structure = pageMaker.getStructure()
#print 'test structure'
#print structure
#On parse
parse('parser.xml', parser_Config)
print parser_Config.tests
#print parser_Config.tests[0]["execs"][0]
#print parser_Config.preprocess_courant

#On verifie que la methode nous renvoi bien la structure apres parsage
structure =parser_Config.getStructure()
print 'test structure'
print structure
