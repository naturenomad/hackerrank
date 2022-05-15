


# Select REGEX Challenges from the Hackerrank site
# Flavour is Python 3.


# MATCHING SPECIFIC STRING
# https://www.hackerrank.com/challenges/matching-specific-string

Regex_Pattern = r'hackerrank'	# Do not delete 'r'.

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))


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

