
# -*- coding: utf-8 -*-
"""Module de generation de rapport xml."""
import sys
reload(sys)
sys.setdefaultencoding("utf_8")
import os
import shutil



def buildKeyValue(doc, key, value):
    """genere les balises feuilles de l arbre xml et leurs contenus."""
    #creation d'une feuille
    keyElt = doc.createElement(key)
    keyElt.appendChild(doc.createTextNode(value))
    return keyElt

def buildParameters(doc, parametersList):
    """genere les balises de parametres de l arbre xml et leurs contenus."""
    #creation d'un noeud parameters
    parametersElt = doc.createElement("parameters")
    print parametersList
    if parametersList!=None :
        #pour chaque parametre
        for key, value in parametersList.items():
            #si le parametre est un tableau
            if key == 'param':
                for val in value:
                    parametersElt.appendChild(buildKeyValue(doc, "parameter", val))
            else :
                parametersElt.appendChild(buildKeyValue(doc, key, value))
                return parametersElt

def serializeCapture(doc, capture):
    """genere les balises de capture de l arbre xml et leurs contenus."""
    #creation d'un noeud capture 
    captureElt = doc.createElement("capture")
    captureElt.appendChild(buildKeyValue(doc, "name", capture["name"]))
    captureElt.appendChild(buildKeyValue(doc, "output", capture["output"]))
    captureElt.appendChild(buildParameters(doc, capture["parameters"]))
    return captureElt

def serializeResult(doc, result):
    """genere les balises de resultats de l arbre xml et leurs contenus."""
    #creation d'un noeud result
    resultElt = doc.createElement("result")
    resultElt.appendChild(buildKeyValue(doc, "message", result["message"]))
    resultElt.appendChild(buildKeyValue(doc, "valid", "%s" % result["valid"]))
    return resultElt

def serializeDiagnostic(doc, diagnostic):
    """genere les balises de diagnostics de l arbre xml et leurs contenus."""
    #creation d'un noeud diagnostic
    diagnosticElt = doc.createElement("diagnostic")
    diagnosticElt.appendChild(buildKeyValue(doc, "name", diagnostic["name"]))
    #s il y a une image de reference 
    if "reference" in diagnostic:
        diagnosticElt.appendChild(buildKeyValue(doc, "reference", diagnostic["reference"]))
    print 'zouzouz'
    print diagnostic
    diagnosticElt.appendChild(buildParameters(doc, diagnostic["parameters"]))
    return diagnosticElt

def serializePreprocessing(doc, preprocessing):
    """genere les balises de preprocessiong de l arbre xml et leurs contenus."""
    #creation d'un noeud preprocessing
    preprocessingElt = doc.createElement("preprocessing")
    preprocessingElt.appendChild(buildKeyValue(doc, "output", preprocessing["output"]))
    #pour chaque filtre
    for filter in preprocessing["filters"]:
        #creation d'un noeud preprocess
        preprocessElt = doc.createElement("preprocess")
        preprocessElt.appendChild(buildKeyValue(doc, "name", filter["name"]))
        preprocessElt.appendChild(buildParameters(doc, filter["parameters"]))
        preprocessElt.appendChild(buildKeyValue(doc, "filter_id", "%s" % filter["filter_id"]))
        preprocessingElt.appendChild(preprocessElt)
    return preprocessingElt

def serializePostprocessing(doc, postprocessing):
    """genere les balises de postprocessing de l arbre xml et leurs contenus."""
    #creation d'un noeud postprocessing
    postprocessingElt = doc.createElement("postprocessing")
    postprocessingElt.appendChild(buildKeyValue(doc, "output", postprocessing["output"]))
    #pour chaque filtre
    for filter in postprocessing["filters"]:
        #creation d'un noeud postprocess
        postprocessElt = doc.createElement("postprocess")
        postprocessElt.appendChild(buildKeyValue(doc, "name", filter["name"]))
        postprocessElt.appendChild(buildParameters(doc, filter["parameters"]))
        postprocessElt.appendChild(buildKeyValue(doc, "filter_id", "%s" % filter["filter_id"]))
        postprocessingElt.appendChild(postprocessElt)
    return postprocessingElt

def serializeComparison(doc, comparison):
    """genere les balises de comparaison de l arbre xml et leurs contenus."""
    #creation d'un noeud comparison
    comparisonsElt = doc.createElement("comparison")
    instancesElt = doc.createElement("instances")
    #pour chaque instance
    for instance in comparison["instances"]:
        #creation d'un noeud instance
        instanceElt= doc.createElement("instance")
        instanceElt.appendChild(buildKeyValue(doc,"instance_id",instance["instance_id"]))
        #construction du noeud preprocessing
        instanceElt.appendChild(serializePreprocessing(doc, instance["preprocessing"]))
        #construction du noeud capture
        instanceElt.appendChild(serializeCapture(doc, instance["capture"]))
        #construction du noeud postprocessing
        instanceElt.appendChild(serializePostprocessing(doc, instance["postprocessing"]))
        
        instanceElt.appendChild(buildKeyValue(doc,"browser",instance["browser"]))
        instancesElt.appendChild(instanceElt)
    
    comparisonsElt.appendChild(instancesElt)
    #construction du noeud result
    comparisonsElt.appendChild(serializeResult(doc, comparison["result"]))
    
    return comparisonsElt

def go(tests, output_file) :
    """genere les balises de tests de l arbre xml et leurs contenus."""
    from xml.dom.minidom import Document
    doc = Document()#creation du document
    doc.appendChild(doc.createProcessingInstruction("xml-stylesheet","type=\"text/xsl\" href=\"xslt/report.xsl\""))
    testsElt = doc.createElement("tests")#creation du noeud "tests"
    doc.appendChild(testsElt)
    #creation des noeuds "test" et de leurs contenus
    for test in tests:
        testElt = doc.createElement("test")
        testsElt.appendChild(testElt)
        #construction du noeud diagnostic
        testElt.appendChild(serializeDiagnostic(doc, test["diagnostic"]))
        
        #creation du noeud "comparisons"
        comparisons = doc.createElement("comparisons")
        #pour chaque instance de comparaison
        for comparison in test["comparisons"]: 
            comparisons.appendChild(serializeComparison(doc, comparison))
        testElt.appendChild(comparisons)
        
    #on genere le fichier xml
    logfile = open(output_file, 'w')
    logfile.write(doc.toprettyxml(indent="  ", encoding="UTF-8"))
    logfile.close()

    print 'Le fichier résultat est', output_file
    # copie de la feuille xsl
    shutil.copyfile('xslt/report.xsl', output_file_xsl)


