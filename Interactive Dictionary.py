#Project 1

import json
from difflib import SequenceMatcher
from difflib import get_close_matches

# r = SequenceMatcher(None, "rainn", "rain").ratio()

fname = 'D:/Code/Python/Projects/01 Interactive Dictionary/076 data.json'
data = open(fname).read()
data_j = json.loads(data)

def Meaning(word):
    return data_j[word]

def output(word):
    arr = Meaning(word)
    for i in arr:
        print(i)

word = input('Enter Word : ')
word = word.lower()

try :
    output(word)
except :
    arr = get_close_matches(word, data_j.keys(), n=1, cutoff=0.7)

    if arr == []:
        print('the word does not exist')
    else:
        deci = input('Did you mean ({}), if yes then type (y) or else type (n) : '.format(arr[0]))
        if deci == 'y':
            output(arr[0])
        else:
            print('the word does not exist')
