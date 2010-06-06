'''
Created on 6 juin 2010

@author: pierrebesson
'''

class Diagnostic(object):
    '''
    classdocs Classe qui permet de definir ce qu'est un diagnostic
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.name=" "
        self.parameters=" "
        self.reference= " "
        self.result= " "
        self.explication = " "
        
    def setName(self,name):
        self.name=name
        
    def setParameters(self,parameters):
        self.parameters=parameters
        
    def setResult(self,result):
        '''
        must be in  {success, failure , unknown}
        '''
        self.result=result
        
    def printIt(self):
        print("Nom",self.name)
        print("parameters",self.parameters)
        print("reference",self.reference)
        print("result",self.result)
        print("explication",self.explication) 
        
        