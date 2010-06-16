from xml.sax.handler import ContentHandler
#from xml.sax import parse
import sys
import copy
class Parser(ContentHandler):
    """Cette classe sert a parser le xml. En fait elle lit le document xml puis:
    A chaque nouvelle balise, la fonction startElement est appelle: elle traite
    l'action a effectuer et les parametres a recuperer dans la balise.
    Ensuite dans la balise la fonction characters sert a recuperer le contenu entre
    cette balise et la suivante ou la balise fermante
    Enfin la balise endElement sert a traiter la fermeture de balise"""
    def __init__(self):
        """
        Cette methode est appele au moment de l'instanciation de la classe elle sert a definir les variables dont on a besoin dans les differentes fonctions appelees dans le parseur 
        """
        #Bolean que verifie que la parsage est fait
        self.parsed = False
        
        #Definition des booleans qui servent a voir au niveau de quel noeud on est
        self.isTests = False
        self.isTest = False
        self.isSource = False
        self.isType = False
        self.isBrowsers = False
        self.isBrowser = False
        self.isPreprocessing = False
        self.isPreprocess = False
        self.isName = False
        self.isParameters = False
        self.isParameter = False
        self.isCapture = False
        self.isInteractions = False
        self.isPostprocess = False
        self.isPostprocessing = False
        self.isDiagnostic = False
        self.isReference = False
        self.n_browsers = 0
        #definition des tableaux de la structure
        self.tests=[]
        self.test_courant={}
        self.preprocess_courant={}
        self.parameters = { }
        self.postprocess_courant={}
        self.preprocessing = []
        self.postprocessing = []
        self.capture = {}
        self.diagnostic = {} 
        
    def startElement(self, name, attrs):
        """
        Cette methode est appele a chaque fois qu'une balise est ouverte <balise> a chaque fois on va mettre le boolean associe a true et creer les structures dont on a besoin
        """
        
        print "start", name

        if name == 'tests':
            self.parsed = True
            self.isTests = True #On met un boolean afin de voir si on est dans la balise Tests
            self.tests=[] #Liste qui contient tous les tests (test1,test2)
            
        elif name == 'test': 
            self.isTest = True
            self.test_courant={}

        elif name == 'source':
            self.isSource = True
            self.source = ''
            
        elif name == 'type':
            self.isType = True
            
        elif name == 'browsers':
            self.isBrowsers = True
            self.n_browsers = 0
            self.test_courant["execs"] = [] 

        elif name == 'browser':
            self.isBrowser = True

        elif name == 'preprocessing':
            self.isPreprocessing = True
            self.preprocessing = []  
            
        elif name == 'preprocess':
            self.isPreprocess = True
            self.preprocess_courant = {}
            
        elif name == 'name':
            self.isName = True
            
        elif name == 'parameters':
            self.parameters = { 'param': []}
            self.isParameters = True

        elif name == 'parameter':
            self.isParameter = True

        elif name == 'capture':
            self.isCapture = True
            self.capture = {}
        elif name == 'interactions':
            self.isInteractions = True

        elif name == 'postprocessing':
            self.isPostprocessing = True
            self.postprocessing = []  
            
        elif name == 'postprocess':
            self.isPostprocess = True
            self.postprocess_courant = {}

        elif name == 'diagnostic':
             self.isDiagnostic = True
             self.diagnostic = {}

        elif name == 'reference':
            self.isReference = True
        

   
            
    def characters(self, chars):
        """
        Cette fonction est appelee au moment on on est dans une balise et que l'on lit le texte compris dans cette balise exemple <balise> text </balise> sert a recuperre le text 
        """
        if self.isSource == True:
            self.source = chars#Attention il faudra le reinitialiser plus tard
        
        elif self.isType == True:
            if chars == "separate" or chars == "compare":
                self.test_courant["type"] = chars #pour ajouter une valeur dans le tableau associtif
                #si le xml n'est pas rempli ou faux on met separate par defaut
            else:
                self.test_courant["type"] = 'separate'
                print >>sys.stderr,'WARNING: THE TYPE WAS EMPTY OR EMPTY '

        elif self.isBrowsers == True:
            if self.isBrowser == True:
                #On donne aux execs le nom du browser pour plus de clarte
                self.test_courant["execs"].append(chars)
                #On ajoute le browser a l'exec
                self.test_courant["execs"][self.n_browsers]={"browser": chars}
                self.n_browsers += 1
       
        elif self.isPreprocessing == True:
            if self.isPreprocess == True:
                if self.isName == True:
                    self.preprocess_courant["name"]=chars
                elif self.isParameters == True:
                    if self.isParameter == True:
                        #self.parameters.append(chars)
                        # M: je prefere stocker les parametres dans le champ 'param'.
                        self.parameters['param'].append(chars)

        elif self.isCapture == True:
            if self.isName == True:
                self.capture["name"]=chars
            elif self.isInteractions == True:
                self.capture["interactions"]=chars
            elif self.isParameters == True:
                if self.isParameter == True:
                        self.parameters['param'].append(chars)

        elif self.isPostprocessing == True:
            if self.isPostprocess == True:
                if self.isName == True:
                    self.postprocess_courant["name"]=chars
                elif self.isParameters == True:
                    if self.isParameter == True:
                        self.parameters['param'].append(chars)

        elif self.isDiagnostic == True:
            
            if self.isName == True:
                print '@@@@@@@@ '
                self.diagnostic["name"]=chars
            elif self.isReference == True:
                print '!!!!!!!!!!!! BOUM'
                self.diagnostic["reference"]=chars
                print chars
            elif self.isParameters == True:
                if self.isParameter == True:
                    self.parameters['param'].append(chars)

    def endElement(self, name):
        """ 
        Cette fonction est appelee au moment de la fermeture de la balise </balise> elle sert a ajouter les sous structures dans la grande structure et a mettre les booleans a false pour le parcours de la structure de l'arbre
        """
        print "end", name
        if name == 'tests':
            self.isTests = False  
            
        elif name == 'test': 
            self.isTest= False
            self.tests.append(self.test_courant)

        elif name == 'source':
            self.isSource = False
            self.test_courant["source"] = self.source            
        elif name == 'type':
            self.isType = False

        elif name == 'browsers':
            self.isBrowsers = False
           
            
        elif name == 'browser':
            self.isBrowser = False

        elif name == 'preprocessing':
            self.isPreprocessing = False
            for i in range(self.n_browsers):
                self.test_courant["execs"][i]["preprocessing"]= {"filters" :copy.deepcopy(self.preprocessing)}

            #print self.test_courant["execs"][0]["preprocessing"]
            
        elif name == 'preprocess':
            self.isPreprocessing = False
            self.preprocess_courant["parameters"] = self.parameters
            self.preprocessing.append(self.preprocess_courant)
           
        elif name == 'name':
            self.isName = False

        elif name == 'parameters':
            self.isParameters = False

        elif name == 'parameter':
            self.isParameter = False

        elif name == 'capture':
            self.isCapture = False
            self.capture["parameters"]=self.parameters
            for i in range(self.n_browsers):
                self.test_courant["execs"][i]["capture"]= copy.deepcopy(self.capture)
            
        elif name == 'interactions':
            self.isInteractions = False

        elif name == 'postprocessing':
            self.isPostprocessing = False
            for i in range(self.n_browsers):
                self.test_courant["execs"][i]["postprocessing"]={"filters" :copy.deepcopy(self.postprocessing)}
            
            
        elif name == 'postprocess':
            self.isPostprocess = False
            self.postprocess_courant["parameters"] = self.parameters
            self.postprocessing.append(self.postprocess_courant)
            print 'post cournat ', self.postprocessing

        elif name == 'diagnostic':
            self.isDiagnostic = False
            self.diagnostic["parameters"]=self.parameters
            #for i in range(self.n_browsers):
            self.test_courant["diagnostic"]= self.diagnostic

        elif name == 'reference':
            self.isReference = False
        
    def getStructure(self):
        if self.parsed == True:
            return self.tests
        else:
            #On gere le cas ou le fichier xml n a pas ete parse on arrete le programme et on explique pourquoi
            print >>sys.stderr,'ERROR: You must parse a XML file first.'
            sys.exit()


