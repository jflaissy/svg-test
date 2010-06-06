'''
Created on 6 juin 2010

@author: pierrebesson
'''

class Capture(object):
    '''
    Classe qui permet de definir une capture 
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.name=' '
        self.source=' '
        self.interactions= ' '
        self.parameters= ' '
        self.output= ' '
        
    def setName(self,name):
            self.name = name
            
    def setSource(self,source):
        self.source = source
    
    def setParameters(self,parameters):
        self.parameters = parameters
        
    def setOutput (self,output):
        self.output = output
        
    def setIntercations(self,interactions):
        self.interactions = interactions
    
    def printIt(self):
        print("Name",self.name)
        print("parameters",self.parameters)
        print("source",self.source)
        print("output",self.output)
        print("interactions",self.interactions) 
    