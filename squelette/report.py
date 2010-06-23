
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf_8")



def buildKeyValue(doc, key, value):
    keyElt = doc.createElement(key)
    keyElt.appendChild(doc.createTextNode(value))
    return keyElt

def buildParameters(doc, parametersList):
    parametersElt = doc.createElement("parameters")
    if parametersList!=None :
        for key, value in parametersList.items():
            parametersElt.appendChild(buildKeyValue(doc, key, value))      
    return parametersElt

def serializeCapture(doc, capture):
    captureElt = doc.createElement("capture")
    captureElt.appendChild(buildKeyValue(doc, "name", capture["name"]))
    captureElt.appendChild(buildKeyValue(doc, "output", capture["output"]))
    captureElt.appendChild(buildParameters(doc, capture["parameters"]))
    return captureElt

def serializeResult(doc, result):
    resultElt = doc.createElement("result")
    resultElt.appendChild(buildKeyValue(doc, "message", result["message"]))
    resultElt.appendChild(buildKeyValue(doc, "valid", "%s" % result["valid"]))
    return resultElt

def serializeDiagnostic(doc, diagnostic):
    diagnosticElt = doc.createElement("diagnostic")
    diagnosticElt.appendChild(buildKeyValue(doc, "name", diagnostic["name"]))
    if "reference" in diagnostic:
        diagnosticElt.appendChild(buildKeyValue(doc, "reference", diagnostic["reference"]))
    diagnosticElt.appendChild(buildParameters(doc, diagnostic["parameters"]))
    return diagnosticElt

def serializePreprocessing(doc, preprocessing):
    preprocessingElt = doc.createElement("preprocessing")
    preprocessingElt.appendChild(buildKeyValue(doc, "output", preprocessing["output"]))
    for filter in preprocessing["filters"]:
        preprocessElt = doc.createElement("preprocess")
        preprocessElt.appendChild(buildKeyValue(doc, "name", filter["name"]))
        preprocessElt.appendChild(buildParameters(doc, filter["parameters"]))
        preprocessElt.appendChild(buildKeyValue(doc, "filter_id", "%s" % filter["filter_id"]))
        preprocessingElt.appendChild(preprocessElt)
    return preprocessingElt

def serializePostprocessing(doc, postprocessing):
    postprocessingElt = doc.createElement("postprocessing")
    postprocessingElt.appendChild(buildKeyValue(doc, "output", postprocessing["output"]))
    for filter in postprocessing["filters"]:
        postprocessElt = doc.createElement("postprocess")
        postprocessElt.appendChild(buildKeyValue(doc, "name", filter["name"]))
        postprocessElt.appendChild(buildParameters(doc, filter["parameters"]))
        postprocessElt.appendChild(buildKeyValue(doc, "filter_id", "%s" % filter["filter_id"]))
        postprocessingElt.appendChild(postprocessElt)
    return postprocessingElt

def serializeComparison(doc, comparison):
    
    comparisonsElt = doc.createElement("comparison")
    instancesElt = doc.createElement("instances")
    for instance in comparison["instances"]:
        instanceElt= doc.createElement("instance")
        instanceElt.appendChild(buildKeyValue(doc,"instance_id",instance["instance_id"]))
        
        instanceElt.appendChild(serializePreprocessing(doc, instance["preprocessing"]))
        instanceElt.appendChild(serializeCapture(doc, instance["capture"]))
        instanceElt.appendChild(serializePostprocessing(doc, instance["postprocessing"]))
        
        instanceElt.appendChild(buildKeyValue(doc,"browser",instance["browser"]))
        instancesElt.appendChild(instanceElt)
    
    comparisonsElt.appendChild(instancesElt)
    comparisonsElt.appendChild(serializeResult(doc, comparison["result"]))
    
    return comparisonsElt

def go(tests, output_file) :
    from xml.dom.minidom import Document
    doc = Document()
    doc.appendChild(doc.createProcessingInstruction("xml-stylesheet","type=\"text/xsl\" href=\"xslt/report.xsl\""))
    testsElt = doc.createElement("tests")
    doc.appendChild(testsElt)

    for test in tests:
        testElt = doc.createElement("test")
        testsElt.appendChild(testElt)
        testElt.appendChild(serializeDiagnostic(doc, test["diagnostic"]))
        
        #serialize comparisons
        comparisons = doc.createElement("comparisons")
        for comparison in test["comparisons"]: 
            comparisons.appendChild(serializeComparison(doc, comparison))
        testElt.appendChild(comparisons)
        
    
    logfile = open(output_file, 'w')
    logfile.write(doc.toprettyxml(indent="  ", encoding="UTF-8"))
    logfile.close()

    print 'Le fichier résultat est', output_file


