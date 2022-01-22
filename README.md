# MergeArabicNames
Merging different transliterations of an Arabic name using Google Translate.

# Features:
1. Processes a list of names with multiple transliterations each.
2. Groups identical Arabic names.
3. Handles the presence/absens of the Article "The" (ال) in the names allowing all to be merged.
4. Prints the output and saves it to a json file.

# Input: 
A list of Arabic names written in English (transliterations) in a .txt file

# Output:
transliterations grouped by their Arabic counterpart in a json format

# Usage:
$ python3 merge_names.py <input_file> <output_file>

# Example:
$ python3 merge_names.py path/to/input/file.txt path/to/output/file.json

# Requirements:

1. <a href="https://www.python.org/downloads/">Python 3.X</a>

2. The following Python Libraries: googletrans, collections, sys, os, io, and json.
