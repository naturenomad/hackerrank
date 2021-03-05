# HACKERRANK's Linux Shell Practice Exercises - Subdomain "Bash"

#############################################
############# BASH ##########################
#############################################

##### LET'S ECHO #######

echo HELLO #HELLO
echo Hi there #Hi there
echo 'Hi there' #Hi there



##### LOOPING AND SKIPPING #######

#!/bin/bash

for value in {1..99..2}
do
  echo $value
done



##### A PERSONALIZED ECHO ########


#!/bin/bash

read name
echo Welcome $name


##### LOOPING WITH NUMBERS #######

#!/bin/bash

for value in {1..50}
do
  echo $value
done


##### THE WORLD OF NUMBERS #######

# Given two integers, x and y, find their sum, difference, product, and quotient.

#!/bin/bash

read x
read y
echo $((x+y)) # sum
echo $((x-y)) # difference
echo $((x*y)) # product
echo $((x/y)) # quotient


##### COMPARING NUMBERS #########

# Given two integers, output :

# Exactly one of the following lines:
# - X is less than Y
# - X is greater than Y
# - X is equal to Y

read x
read y

if [ $x -lt $y ]
then
  echo X is less than Y
elif [ $x -gt $y ]
then
  echo X is greater than Y
else
  echo X is equal to Y
fi


###### GETTING STARTED WITH CONDITIONALS ###############


# Read in one character from STDIN.
# If the character is 'Y' or 'y' display "YES".
# If the character is 'N' or 'n' display "NO".
# No other character will be provided as input. 

read -n1 x

if [ $x = y ] || [ $x = Y ]
then
  echo YES
elif [ $x = n ] || [ $x = N ]
then
  echo NO
fi



###### MORE ON CONDITIONALS ###############

# Given three integers (x, y, and z) representing the three sides of a triangle, identify whether the triangle is 
# scalene, isosceles, or equilateral.
#    If all three sides are equal, output EQUILATERAL.
#    Otherwise, if any two sides are equal, output ISOSCELES.
#    Otherwise, output SCALENE.


#!/bin/bash
read x
read y
read z
 
if [ $x -eq $y ] && [ $x -eq $z ];
then
  echo "EQUILATERAL"
elif ( [ $x -eq $y ] && [ $x -ne $z ] ) || ( [ $x -eq $z ] && [ $x -ne $y ] ) || ( [ $y -eq $z ] && [ $x -ne $y ] );
then
  echo "ISOSCELES"
else
  echo "SCALENE"
fi



###### ARITHMETIC OPERATIONS ###############

# A mathematical expression containing +,-,*,^, / and parenthesis will be provided. 
# Read in the expression, then evaluate it. Display the result rounded to decimal places. 

#!/bin/bash

read math

echo $math | bc -l | xargs printf "%.3f"



###### COMPUTE THE AVERAGE ###############

# Given N integers, compute their average, rounded to three decimal places. 

#!/bin/bash

sum=0
read lines

for line in $(seq $lines);
do
  read num
  sum=$(( sum + num ))
done

echo "$sum/$lines" | bc -l | xargs printf "%.3f"



########## FUNCTIONS AND FRACTALS - RECURSIVE TREES - BASH! ###################

# TBD

