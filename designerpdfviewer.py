##############################################################
#### DESIGNER PDF VIEWER #####################################

# https://www.hackerrank.com/challenges/designer-pdf-viewer

# designerPdfViewer has the following parameter(s):

#    int h[26]: the heights of each letter
#    string word: a string

# Calculate 'height' - length of word x highest letter


#!/bin/python3

import math
import os
import random
import re
import sys
import string


def designerPdfViewer(h, word):
    alphabetHeights = dict(zip(list(string.ascii_lowercase), h))
    wordHeight = 0
    for j in word :
        if alphabetHeights[j] > wordHeight : 
            wordHeight = alphabetHeights[j]
    return wordHeight*len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()


# Test cases
h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
word = 'abc'
# 9

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7]
word = 'zaba'
# 28

