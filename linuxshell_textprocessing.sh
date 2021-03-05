
#############################################
############# TEXT PROCESSING ###############
#############################################


########## CUT #1 ###################

# Given N lines of input, print the 3rd character from each line as a new line of output.

# I've added an exit clause to avoid needing ctrl-c :

#!/bin/bash

while true;
do
  read s
  if [ ${#s} -gt 0 ];
  then
    echo $s | cut -c3
  else
    break
  fi
done



########## CUT #2 ###################

# Display the 2nd and 7th character from each line of text. 

while read s;
do
  echo $s | cut -c2,7
done


# Alternative : Doesn't need the while loop, take stdin as default : can simply do :

cut -c2,7


########## CUT #3 ###################

# Display a range of characters starting at the position of a string and ending at the position 
# (both positions included).

cut -c2-7


########## CUT #4 ###################

# Display the first four characters from each line of text. 

cut -c1-4


########## CUT #5 ###################

# Given a tab delimited file with several columns (tsv format) print the first three fields.

cut -f1-3  # tabs is the default delimiter

# Alternative, specifying tabs :

cut -d$'\t' -f1-3



########## CUT #6 ###################

# Print the characters from thirteenth position to the end.

cut -c13-



########## CUT #7 ###################

# Given a sentence, identify and display its fourth word. Assume that the space (' ') is the only delimiter between words.

cut -d$' ' -f4


# Alternative :

cut -d ' ' -f4


########## CUT #8 ###################

# Given a sentence, identify and display its first three words. Assume that the space (' ') is the only delimiter between words. 

cut -d ' ' -f1-3


########## CUT #9 ###################

# Given a tab delimited file with several columns (tsv format) print the fields from second fields to last field.

cut -f2-


########## HEAD OF A TEXT FILE #1 ###################

# Display the first 20 lines of an input file.

head -n 20 filename


# Alternative, for stdin :

head -n 20


########## HEAD OF A TEXT FILE #2 ###################

# Display the first characters of an input file.

head -c 20


########## MIDDLE OF A TEXT FILE ###################

# Display the lines (from line number 12 to 22, both inclusive) of a given text file.

head -n 22 | tail -n +12


# NOTE :  tail -n 12 -> outputs last 12 lines 
#         tail -n +12 -> outputs all lines starting from line 12


# Alternative, since -n is the default selector :

head -22 | tail +12


########## TAIL OF A TEXT FILE #1 ###################

# Display the last 20 lines of an input file.

tail -20


########## TAIL OF A TEXT FILE #2 ###################

# Display the last 20 characters of an input file.

tail -c -20



########## 'TR' COMMAND #1 ###################

# tr - translate or delete characters

# In a given fragment of text, replace all parentheses () with box brackets [].

tr '( )' '[ ]'


########## 'TR' COMMAND #2 ###################

# In a given fragment of text, delete all the lowercase characters a-z.

tr -d 'a-z'

tr -d [:lower:]


########## 'TR' COMMAND #3 ###################

# In a given fragment of text, replace all sequences of multiple spaces with just one space.

tr -s ' '


########## SORT COMMAND #1 ###################

# Given a text file, order the lines in lexicographical order.

sort -d # dictionary

# Alternative, since by default, the sort command sorts file assuming the contents are ASCII :

sort


########## SORT COMMAND #2 ###################

# Given a text file, order the lines in reverse lexicographical order (i.e. Z-A instead of A-Z).

sort -d -r

# Alternatively (-d is default) :

sort -r


########## SORT COMMAND #3 ###################

# Output the text file with the lines reordered in numerically ascending order. 

sort -n



########## SORT COMMAND #4 ###################

# Output lines re-ordered in descending order (numerically). 

sort -rn


########## SORT COMMAND #5 ###################

# Rearrange the rows of the table in descending order of the values provided in the second column.

# NOTE : In sort you need to specify the column delimiter, default is space, -t is the field seperator selector

sort -t$'\t' -k2 -rn


########## SORT COMMAND #6 ###################

# Sort the data in ascending numerical order of the second column

sort -t$'\t' -k2 -n



########## SORT COMMAND #7 ###################

# From pipe-delimitedSort the data in descending numerical order of the second column

sort -t$'|' -k2 -rn


########## UNIQ COMMAND #1 ###################

# Given a text file, remove the consecutive repetitions of any line.

uniq

########## UNIQ COMMAND #2 ###################

# Given a text file, count the number of times each line repeats itself. 
# Only consider consecutive repetitions. Display the space separated count and line, respectively. 
# There shouldn't be any leading or trailing spaces.

uniq -c | sed 's/^ *//g'



########## UNIQ COMMAND #3 ###################

# Given a text file, count the number of times each line repeats itself (only consider consecutive repetions).
# Display the count and the line, separated by a space. There shouldn't be leading or trailing spaces. 

# This time, compare consecutive lines in a case insensitive manner. 

uniq -ic | sed 's/^ *//g'


########## UNIQ COMMAND #4 ###################

# Given a text file, display only those lines which are not followed or preceded by identical replications. 

uniq -u



########## PASTE - 3  ###################

# Replace the newlines in the input with tabs.

paste -s

# paste - merge lines of files
#       Write  lines  consisting  of  the sequentially corresponding lines from
#       each FILE, separated by TABs, to standard output.
#
#       -s, --serial paste one file at a time instead of in parallel



########## PASTE - 4  ###################

# Restructure the file in such a way, that every group of three consecutive rows are folded into one, and separated by tab. 

# -d express how to delimit output :
paste -sd $'\t\t\n'


########## PASTE - 1  ###################

# Replace the newlines in the input file with semicolons.

paste -sd $';'


########## PASTE - 2  ###################

# Restructure the file so that three consecutive rows are folded into one line and are separated by semicolons. 

paste -sd $';;\n'


