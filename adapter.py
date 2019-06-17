import json

def replaceInJson(dct):
    result = dict((key.replace("-", "_"), value) for (key, value) in dct.items())
    return result

def adoptJsonToAngular(data):
    return json.loads(data, object_hook=replaceInJson)