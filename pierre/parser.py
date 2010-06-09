from xml.sax.handler import ContentHandler
from xml.sax import parse
class PageMaker(ContentHandler): 
    passthrough = False 
    def startElement(self, name, attrs):
        if name == 'tests': 
            self.passthrough = True
            self.tests=[]
            
        if name == 'test': 
            self.test= True
            self.testcourant={}
            
        if name=='type'
            self.testcourant.[name] = name #pour ajouter une valeur dans le tableau associtif
            
            
                
    def endElement(self, name): 
        if name == 'tests':
            self.passthrough = False  
            
        if name == 'test': 
            self.test= False    
            self.tests.append(test_courant)
               
    def characters(self, chars): 
        if self.passthrough: self.out.write(chars)


parse('parser.xml', PageMaker ())