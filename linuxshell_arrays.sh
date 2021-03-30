

#############################################
############# ARRAYS ########################
#############################################


########## READ IN AN ARRAY  ###################

# Given a list of countries, each on a new line, read them into an array and then display the entire array, with a space between each of the countries' names. 


#!/bin/bash

counter=0
while read country
do
  countries[$counter]=$country
  ((counter+=1))
done

echo ${countries[@]}



# Faster alternative :

countries=($(cat))
echo ${countries[@]}



########## SLICE AN ARRAY  ###################

# Given a list of countries, each on a new line, read them into an array. Then slice the array and display only the elements lying between positions 3 and 7, both inclusive.

#!/bin/bash

counter=0
while read country
do
  countries[$counter]=$country
  ((counter+=1))
done

echo ${countries[@]:3:5}


########## FILTER AN ARRAY WITH PATTERNS ###################

# Given a list of countries, each on a new line, read them into an array and then filter out (remove) all the names containing the letter 'a' or 'A'. 


#!/bin/bash

counter=0
while read country
do
  countries[$counter]=$country
  ((counter+=1))
done

# Use parameter expansion, look for array entries containing a or A and replace with nothing
echo ${countries[@]/*[aA]*/}


# Alternative to achieve the goal, but this uses a file rather than an array :

cat > countries
grep -iv a countries



########## CONCATENATE AN ARRAY WITH ITSELF ###################

# Given a list of countries, each on a new line, read them into an array. 
# Then, concatenate the array with itself (twice) - so there a total of three repetitions of the original array - 
# and then display the entire concatenated array, with a space between each of the countries' names.

#!/bin/bash

readarray -t countries

countries=( "${countries[@]}" "${countries[@]}" "${countries[@]}" )

echo "${countries[@]}"


########## DISPLAY AN ELEMENT OF AN ARRAY ###################

# Given a list of countries, each on a new line, read them into an array and then display the element indexed at 3.

#!/usr/bin/env bash

readarray -t countries

echo "${countries[3]}"

