'''
Created on 6 juin 2010

@author: pierrebesson
'''

class Preprocess(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.name = " "
        self.parameters= " "
        self.output= " "
         
    def setName(self,name):
            self.name = name
            
    def setParameters(self,parameters):
        self.parameters = parameters
    
    def setOutput (self,output):
        self.output = output
    
    def printIt(self):
        print("Nom",self.name)
        print("parameters",self.parameters)
        print("output",self.output)
        