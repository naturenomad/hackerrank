

#############################################
############# GREP SED AWK ##################
#############################################

### Awk - 1 ###

# Given a file with four space separated columns containing the scores of students in three subjects. 
# The first column contains a single character (A-Z), the student identifier. 
# The next three columns have three numbers each. The numbers are between 0 and 100, both inclusive. 
# These numbers denote the scores of the students in English, Mathematics, and Science, respectively.

# Task is to identify those lines that do not contain all three scores for students. 

# For each student, if one or more of the three scores is missing, display:
# Not all scores are available for [Identifier]

#!/usr/bin/env bash

awk '{
    if ($2=="" || $3=="" || $4=="")
    printf "Not all scores are available for "$1"\n"
}' # bash1.txt



########## AWK - 3 ###################

# There are a lot of quick tricks which may be accomplished with the 'awk' interpreter. 
# Among other things, awk may be used for a lot of text-munging and data-processing tasks which require some quick scripting work.

# Provided a file with four space-separated columns containing the scores of students in three subjects. 
# The first column, contains a single character (A-Z) - the identifier of the student. 
# The next three columns have three numbers (each between 0 and 100, both inclusive) which are the scores of the 
# students in English, Mathematics and Science respectively. 

# Identify the performance grade for each student. If the average of the three scores is 80 or more, the grade is 'A'. 
# If the average is 60 or above, but less than 80, the grade is 'B'. If the average is 50 or above, but less than 60, 
# the grade is 'C'. Otherwise the grade is 'FAIL'.

# For each row of data, append a space, a colon, followed by another space, and the grade. 

awk '{
    avg=($2+$3+$4)/3;
    print $0, ":", (avg<50)?"FAIL":(avg<60)?"C":(avg<80)?"B":"A";
}' # filename


########## AWK - 4 ###################

# Same file as AWK - 3 : Concatenate every 2 lines of input with a semi-colon.

awk '{
    if ( NR%2 == 0) 
    printf $0"\n" 
    else 
    printf $0";";
}' # filename


# One line alternative using pattern{action}, 
# NR%2 = Odd lines (True when there is a remainder)
# 1-NR%2 = Even lines (True when there is no remainder).

awk 'NR%2{printf$0";"}1-NR%2{printf$0"\n"}' bash.txt

# Because the second part is the default behaviour can be shortened to -

awk 'NR%2{printf$0";"}1-NR%2'


########## GREP #1 ###################

# https://youtu.be/WX5Zfflvdt0 - 52 minute video on regular expressions, sed, grep etc.

# Grep is a multi-purpose search tool that is used to find specified strings or regular expressions. 
# A variety of options exist that makes it possible to use this command in several different ways and to handle many different situations. 
# For example, one might opt for a case-insensitive search, or to display only the fragment matching the specified search pattern. 
# The command could also be used to display only the line number of an input file where the specified string or regular expression has been found.

# Before using grep, be familiar with regular expressions to be able to harness the command to its fullest. 

# Output only those lines that contain the word 'the'. The search should be case sensitive. 
# The relative ordering of the lines in the output should be the same as it was in the input. 

grep '\bthe\b' #filename, \b is word boundary

grep -w 'the' #filename


########## GREP #2 ###################

# Output only those lines that contain the word 'the'. The search should NOT be case sensitive. The relative ordering of the lines in the output should be the same as it was in the input. 

grep -iw 'the' #filename


########## GREP #3 ###################

# Only display those lines that do NOT contain the word 'that'. The relative ordering of the lines should be the same as it was in the input file. 

grep -iv 'that' #filename



########## GREP - A ###################

# Use grep to display all those lines which contain any of the following words in them:
# the, that, then, those
# The search should not be sensitive to case. Display only those lines of an input file, which contain the required words. 

grep -iw -e the -e that -e then -e those # filename

# Or 

grep -iwE 'the|that|then|those' # filename


########## GREP - B ###################

# Given an input file, with N credit card numbers, each in a new line
# Task is to grep out and output only those credit card numbers which have two or more 
# consecutive occurences of the same digit (which may be separated by a space, if they are in different segments). 
# Assume that the credit card numbers will have 4 space separated segments with 4 digits each.

# Take any char . and remember it (....), \1+ repeat stored digit at least once, ignores spaces.

grep -E '(.)\1+' # filename

# The above works on my system GNU bash, version 4.4.20(1)-release (x86_64-pc-linux-gnu), but not on the Hackerrank shell. Suspect spaces not ignored.

# Alternative :

grep -E '(.) *\1' # filename

# The above also doesn't work on Hackerrank.
# Try without -E

grep '\(.\) *\1' # filename


########## SED COMMAND #1 ###################

# Examples :

# Substitute first occurance :
 sed -e s/editor/tool/
 
 # Substitute all occurrances :
 sed -e s/editor/tool/g
 
 # Substitute second occurrance :
 sed -e s/editor/tool/2
 
 # Put braces around all occurrances :
 sed -e s/editor/{\&}/g
 
 # For each line in a given input file, transform the first occurrence of the word 'the' with 'this'. 
 # The search and transformation should be strictly case sensitive. 
 
 # Need the quotemarks once adding regexps.

sed -e 's/\<the\>/this/' # bash.txt | grep this


########## SED COMMAND #2 ###################

# For each line in a given input file, transform all the occurrences of the word 'thy' with 'your'. 
# The search should be case insensitive.

sed -e 's/\<thy\>/your/Ig' # I works only on GNU Linux



########## SED COMMAND #3 ###################

# Given an input file, in each line, highlight all the occurrences of 'thy' by wrapping them up in brace brackets. 
# The search should be case-insensitive.

 sed -e s/thy/{\&}/Ig # bash.txt | grep '{'
 


########## SED COMMAND #4 ###################

# Task

# Given lines of credit card numbers, mask the first digits of each credit card number with an asterisk (i.e., *) 
# and print the masked card number on a new line. 
# Each credit card number consists of four space-separated groups of four digits. 
# For example, the credit card number 1234 5678 9101 1234 would be masked and printed as **** **** **** 1234.

# Building this up :

cat bash.txt | sed -e s/[0-9]/*/1
# *234 5678 9101 1234

cat bash.txt | sed -re 's/[0-9]{4}/****/1'
**** 5678 9101 1234
# -r : option removes the usage of backslash for escaping of opening '(' or '{' and '}' or ')' closing brackets
# NOTE : -r has to come before -e

cat bash.txt | sed -re 's/[0-9]{4}/****/1' | sed -re 's/[0-9]{4}/****/1' | sed -re 's/[0-9]{4}/****/1'

# For Hackerrank :

sed -re 's/[0-9]{4}/****/1' | sed -re 's/[0-9]{4}/****/1' | sed -re 's/[0-9]{4}/****/1'


# Also works -
cat bash.txt | rev | sed 's/[0-9]/*/g5' | rev
