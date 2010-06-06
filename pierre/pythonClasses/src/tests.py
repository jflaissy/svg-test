'''
Created on 6 juin 2010

@author: pierrebesson
'''

class Tests(object):
    '''
    classdocs Classe qui contient toute la description des tests
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.useragent="firefox"
        self.type=" "
        self.tests = []
        
    def setUseragent(self,useragent):
        self.useragent = useragent;
    
    def addTest(self,test):
        self.tests.append(test)
    
    def setType(self,type):
        self.type = type;
        
    def printIt(self):
        print("useragent",self.useragent)
        print("type",self.type)
        print("tests",self.tests)