#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
import io
import json
import os
import sys

from googletrans import Translator


def translate_names(input_list):
    translator = Translator() 
    result = {} 
    transliterations = translator.translate(input_list, src='en', dest='ar')
    for transliteration in transliterations:
        arabic_name = transliteration.text
        result[transliteration.origin] = arabic_name
    return result

    
def reverse_dict(input_dict): 
    result = defaultdict(list)
    for key, value in input_dict.items():
        result[value].append(key)
    return result


def handle_article_the(input_dict):

    dupes = {}
    for key, value in input_dict.items():
        if(key[0] == "ا" and key[1] == "ل"):
            dupes[key[2:]] = value

    duped_keys = []
    for key, value in input_dict.items():
        for duped_key, duped_value in dupes.items():
            if(duped_key == key):
                input_dict[key] = input_dict[key] + dupes[key]
                the_key = "ال" + key
                duped_keys.append(the_key)
            
    for key in duped_keys:
        del input_dict[key]
            
    return input_dict


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 merge_names.py <input_file> <output_file>")
        print("e.g: python3 merge_names.py path/to/input/file.txt path/to/output/file.json")
        exit()
        
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
if not os.path.exists(input_file_name):
    print("input file does not exist. Make sure the path is correct and try again!")
    exit()
if not os.path.exists(output_file_name):
    print("Output file does not exist. One will be created under the name (output.json)")
    output_file_name = "output.json"
    
if output_file_name[-5:].lower() != ".json":
    print("Output file must be json. One will be created under the name (output.json)")
    output_file_name = "output.json"
    
with io.open(input_file_name, 'r', newline=None) as input_file:
    names = []
    for line in input_file:
        line = line.replace("\n", "")
        names.append(line)
        
translated_names_dict = translate_names(names)
reversed_translated_names = reverse_dict(translated_names_dict)
output = handle_article_the(reversed_translated_names)

for arabic_name, english_names in output.items():
    print(arabic_name, ": " , english_names)

with open(output_file_name, "w", encoding='utf8') as output_file:
    json.dump(output, output_file, ensure_ascii=False)

