from xml.sax.handler import ContentHandler
from xml.sax import parse
class PageMaker(ContentHandler): 
    passthrough = False 
    def startElement(self, name, attrs):
        if name == 'tests': 
            self.passthrough = True 
            self.out = open(name + '.py', 'w') 
            self.out.write(name+'[] \n')
            
        if name == 'test': 
            self.test= True
            self.out.write(tests.append())
                
    def endElement(self, name): 
        if name == 'tests':
            self.passthrough = False  
            self.out.close()
        if name == 'test': 
            self.test= False    
               
    def characters(self, chars): 
        if self.passthrough: self.out.write(chars)

parse('parser.xml', PageMaker ())