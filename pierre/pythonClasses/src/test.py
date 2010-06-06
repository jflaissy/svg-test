import capture
#import diagnostic
import preprocess



class Test(object):
    "Define what is a test"
    def __init__(self):
        self.type="type"
        self.diagnostics=[]#Ici on aura une liste d'object Diagnostic
        self.capture = capture#On fait appel a un objet capture
        self.preprocess = preprocess#On fait appel a un objet Pretraitement
        
    def setType(self,type):
        self.type = type
    def addDiagnostic(self, diagnostic):
        self.diagnostics.append(diagnostic)
        
    def setCapture(self,capture):
        self.capture = capture
        
    def setPreprocess(self,preprocess):
        self.preprocess=preprocess
    def printIt(self):
        print("Type=",self.type)
        print("Diagnostic",self.diagnostics)
        print("Capture", self.capture)
        print("Preprocess",self.preprocess)
        
