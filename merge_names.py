#!/usr/bin/env python
# -*- coding: utf-8 -*-
from googletrans import Translator
from collections import defaultdict
import sys
import os
import io
import json

def translateNames(inputList):
    translator = Translator() 
    result = {} 
    transliterations = translator.translate(names, src='en', dest='ar')
    for transliteration in transliterations:
        arabicName = transliteration.text
        result[transliteration.origin] = arabicName
    return result
    
def reverseDict(inputDict):    
    result = defaultdict(list)
    for key, value in inputDict.items():
        result[value].append(key)
    return result

def handleArticleThe(inputDict):
    dupes = {}
    for key, value in inputDict.items():
        if(key[0] == "ا" and key[1] == "ل"):
            dupes[key[2:]] = value

    dupedKeys = []
    for key, value in inputDict.items():
        for dupedKey, dupedValue in dupes.items():
            if(dupedKey == key):
                inputDict[key] = inputDict[key] + dupes[key]
                theKey = "ال" + key
                dupedKeys.append(theKey)
            
    for key in dupedKeys:
        del inputDict[key]
            
    return inputDict

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 merge_names.py <input_file> <output_file>")
        print("e.g: python3 merge_names.py path/to/input/file.txt path/to/output/file.json")
        exit()
        
inputFileName = sys.argv[1]
outputFileName = sys.argv[2]

if not os.path.exists(inputFileName):
    print("input file does not exist. Make sure the path is correct and try again!")
    exit()
    
if not os.path.exists(outputFileName):
    print("Output file does not exist. One will be created under the name (output.json)")
    outputFileName = "output.json"
    
if outputFileName[-5:].lower() != ".json":
    print("Output file must be json. One will be created under the name (output.json)")
    outputFileName = "output.json"
    
with io.open(inputFileName, 'r', newline=None) as inputFile:
    names = []
    for line in inputFile:
        line = line.replace("\n", "")
        names.append(line)
        
translatedNamesDict = translateNames(names)
reversedTranslatedNames = reverseDict(translatedNamesDict)
output  = handleArticleThe(reversedTranslatedNames)

for arabicName, englishNames in output.items():
    print(arabicName, ": " ,englishNames)

with open(outputFileName, "w",encoding='utf8') as outputFile:
    json.dump(output, outputFile, ensure_ascii = False)
