import json
import os


def loadfromsave():
    try:
        jsonfile = open("save.json", "r",encoding='UTF-8')
    except:
        defaultdata = loadfromdefault()
        savetojson(defaultdata)
        jsonfile = open("save.json", "r",encoding='UTF-8')
    try:
        data = json.load(jsonfile)
        jsonfile.close()
        return data
    except:
        return None

def loadfromdefault():
    try:
        jsonfile = open("default.json", "r", encoding='UTF-8')
        data = json.load(jsonfile)
        jsonfile.close()
        return data
    except:
        return None

def loadfromtranslate():
    try:
        jsonfile = open("translate.json", "r", encoding='UTF-8')
        data = json.load(jsonfile)
        jsonfile.close()
        return data
    except:
        return None

def savetojson(data):
    jsonfile = open("save.json", "w+",encoding='UTF-8')
    json.dump(data,jsonfile)
    jsonfile.close()


