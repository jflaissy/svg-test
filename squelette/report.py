

def buildKeyValue(doc, key, value):
    keyElt = doc.createElement(key)
    keyElt.appendChild(doc.createTextNode(value))
    return keyElt

def buildParameters(doc, parametersList):
    parametersElt = doc.createElement("parameters")
    if parametersList!=None :
        for parameter in parametersList:
            parametersElt.appendChild(buildKeyValue(doc, "parameter", parameter))       
    return parametersElt

def serializeCapture(doc, capture):
    captureElt = doc.createElement("capture")
    captureElt.appendChild(buildKeyValue(doc, "name", capture["name"]))
    captureElt.appendChild(buildKeyValue(doc, "output", capture["output"]))
    captureElt.appendChild(buildParameters(doc, capture["parameters"]))
    return captureElt

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

def serializePostprocess(doc, postprocessing):
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
        instanceElt.appendChild(serializePreprocessing(doc, instance["postprocessing"]))
        
        instanceElt.appendChild(buildKeyValue(doc,"browser",instance["browser"]))
        instancesElt.appendChild(instanceElt)
    
    comparisonsElt.appendChild(instancesElt)
    
    return comparisonsElt

def go(tests, output_file) :
    from xml.dom.minidom import Document
    doc = Document()
    testsElt = doc.createElement("tests")
    doc.appendChild(testsElt)

    for test in tests:
        testElt = doc.createElement("test")
        testsElt.appendChild(testElt)

        #serialize comparisons
        comparisons = doc.createElement("comparisons")
        for comparison in test["comparisons"]: 
            comparisons.appendChild(serializeComparison(doc, comparison))
        testElt.appendChild(comparisons)
    
    logfile = open(output_file, 'w')
    logfile.write(doc.toprettyxml(indent="    "))
    logfile.close()



