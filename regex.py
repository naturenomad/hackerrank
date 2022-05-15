
# REGEX Challenges from the Hackerrank site
# Flavour is Python 3.


################################################################
# MATCHING SPECIFIC STRING
# https://www.hackerrank.com/challenges/matching-specific-string

Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))


###########################################################################
# MATCHING DIGITS AND NON-DIGIT CHARACTERS
# https://www.hackerrank.com/challenges/matching-digits-non-digit-character

# \d matches any digit [0-9]
# \D matches any character that is not a digit

# Match the pattern xxXxxXxxxx where x is a digit and X is a non-digit :

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())

# Test cases :
#06-11-2015
# true


####################################################################################
# MATCHING WHITESPACE AND NON-WHITESPACE CHARACTERS
# https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character

# \s matches any whitespace character [ \r\n\t\f ]
# \S matches any non-white space character

# match the pattern XXxXXxXX
# Where x denotes whitespace characters, and X denotes non-white space characters.

Regex_Pattern = r"\S\S\s\S\S\s\S\S"

# Test case 
#12 11 15
# true


######################################################################
# MATCHING WORD AND NON-WORD CHARACTERS
# https://www.hackerrank.com/challenges/matching-word-non-word/problem

# \w will match any word character.
# Word characters include alphanumeric characters (-, - and -) and underscores (_).
# \W matches any non-word character.

# match the pattern xxxXxxxxxxxxxxXxxx
# Where x denotes any word character and X denotes any non-word character.

Regex_Pattern = r"\w{3}\W\w\{10}W\w{3}"

# Test case
#www.hackerrank.com
# true


##################################################################
# MATCHING START AND END
# https://www.hackerrank.com/challenges/matching-start-end/problem

# The ^ symbol matches the position at the start of a string.
# The $ symbol matches the position at the end of a string.

# match the pattern Xxxxx.
# Where x denotes a word character, and X denotes a digit. 

Regex_Pattern = r"^\d\w{4}.$"

# Test case 
#0qwer.
# true


######################################################################
# MATCH ANYTHING BUT A NEWLINE
# https://www.hackerrank.com/challenges/matching-anything-but-new-line

# The dot (.) matches anything (except for a newline).

# Write a regular expression that matches only and exactly strings of form: abc.def.ghi.jkx 
# where each variable can be any single character except the newline.

regex_pattern = r"^...\....\....\....$"	# Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())

# Test cases
#123.456.abc.def
# true

#123.123.123.132.123.123
# false


#################################################
# THE BRITISH AND AMERICAN STYLE OF SPELLING
# https://www.hackerrank.com/challenges/uk-and-us

# Given a string, and a test word with the American ending (-ze), find the number of cases of either 
# the British or American spelling.

# Input Format
# First line contains N, N lines follow each line contains a sequence of words (W) separated by a 
# single space. Next line contains T. T testcases follow in a new line. Each line contains the 
# American English spelling of a word (W')

# Constraints
#
# 1 <= N <= 10 : Each line doesn't contain more than 10 words (W)
# Each character of W and W' is a lowercase alphabet.
# If C is the count of the number of characters of W or W', then
# 1 <= C <= 20
# 1 <= T <= 10
# W' ends with ze ( US version of the word) 

# Output Format
#
# Output T lines and in each line output the total number of American and British versions of (W') in # all of N lines that contains a sequence of words.

import re

def stylesCount() :
    # Get string
    lines = int(input())
    s = ""
    for i in range(lines) :
        s+= input() + "\n"
    
    # Get test word(s) and their Gbr version, put in a list : 
    numtests = int(input())
    tests=[]
    for i in range(numtests) :
        w = input()
        tests.append([w, w[:-2] + "se"])
        
    # For each test word combination, count occurances
    for i in tests :
        n = 0
        for j in i :
            n+= len(re.findall(j, s))
        print(n)

# ... or more efficient alternative ...

def stylesCount() :
    # Get string
    lines = int(input())
    s = ""
    for i in range(lines) :
        s+= input() + "\n"
    
    # Get test word(s) and their Gbr version, put in a list : 
    numtests = int(input())
    tests=[]
    for i in range(numtests) :
        w = input()
        print(len(re.findall(w[:-2] + '[sz]e', s)))

# Test case
stylesCount()
2
hackerrank has such a good ui that it takes no time to familiarise its environment
to familiarize oneself with ui of hackerrank is easy
1
familiarize

