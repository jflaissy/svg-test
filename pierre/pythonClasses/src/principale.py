'''
Created on 6 juin 2010

@author: pierrebesson
'''
import tests
import test
import capture
import diagnostic
import preprocess

#On se fait un nouveau gros test
tests= tests.Tests()
tests.printIt()


 #Creons un petit test
test=test.Test()
test.setType("Static")
#on se fait un diagnostic
diag=diagnostic.Diagnostic()
diag.setParameters("parametres")
diag.setResult("result")
diag.setName("name")
diag.printIt()
test.addDiagnostic(diag)

test.printIt()


 