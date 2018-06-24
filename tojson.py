import json
import os


def loadfromjson():
    try:
        jsonfile = open("save.json", "r",encoding='UTF-8')
    except:
        jsonfile = open("save.json", "w+",encoding='UTF-8')
        jsonfile.close()
        jsonfile = open("save.json", "r",encoding='UTF-8')
    try:
        data = json.load(jsonfile)
        jsonfile.close()
        return data
    except:
        return None

def savetojson(data):
    jsonfile = open("save.json", "w+",encoding='UTF-8')
    json.dump(data,jsonfile)
    jsonfile.close()


