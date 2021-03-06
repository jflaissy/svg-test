'''
Created on 8 juin 2010

@author: pierrebesson
'''
tests=[]
#ici c'est un tableau associatif


preprocess = {
             "name":"name du preprocess",
             "parameters": ["parameter1","parameter2"]
             }
capture = {
        "name":"module name",
        "interactions": "interaction script",
        "parameters": ["parameter1","parameter2"]        
        }

postprocess= {
             "name" : "name du preprocess",
             "parameters" : ["parameter1","parameter2"],
             "source" : "file.svg" 
             }

exec1 = {
        "preprocessing": { "filters" : [preprocess] }#1,preprocess2,preprocess3],
        "capture": capture,
        "postprocessing": { "filters" : [postprocess] },#,postprocess2,postprocess3],
        "browser": "firefox"
        }

diagnostic = {
              "name":"nom du module",
              "parameters": ["parameter1","parameter2"],
              "reference": "file_ref.png"

              }

test_courant = {
                "type":"les uns contre les autres",
                "execs": [exec1],#,exec2,exec3],
                "diagnostic": diagnostic
                }
#pour appeler un champ de test_courant
test_courant["type"]="type def"
#definition des execs

tests.append(test_courant)
