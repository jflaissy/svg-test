'''
Created on 8 juin 2010

@author: pierrebesson
'''
tests=[]
#ici c'est un tableau associatif


preprocess = {
             'name':'text-delete',
             'parameters': ['parameter1-pre','parameter2-pre']
             }
capture = {
        'name':'static-cap',
        'interactions': 'interaction script',
        'parameters': ['parameter1','parameter2']        
        }

postprocess= {
             'name':'crop-static',
             'parameters': ['parameter1','parameter2']
             }

exec1 = {
        'preprocessing': { 'filters' : [preprocess,
                                        { 'name' : 'add-square', 'parameters' : None }] },
        'capture': capture,
        'postprocessing':{'filters' : [postprocess]},#,postprocess2,postprocess3],
        'browser': 'firefox'
        }

diagnostic = {
              'name':'nom du module',
              'parameters': ['parameter1','parameter2'],
              'reference': 'file_ref.png'
              }

test_courant = {
                'type':'les uns contre les autres',
                'execs': [exec1],#,exec2,exec3],
                'diagnostic': diagnostic
                }
#pour appeler un champ de test_courant
test_courant['type']='type def'
test_courant['source'] = 'source.svg' # TODO(m): verifier avec P.
#definition des execs

tests.append(test_courant)

def getExample():
    return tests
