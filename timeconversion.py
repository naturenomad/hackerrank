# TIME CONVERSION

# timeConversion(s) takes an AM/PM time string and returns as 24-hour format

#!/bin/python3

import os
import sys
import datetime as dt

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    return(dt.datetime.strptime(s,'%I:%M:%S%p').strftime('%H:%M:%S'))

#s = dt.datetime.now().strftime('%I:%M:%S%p')
# or
#s='07:05:45PM'
#print(timeConversion(s))


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    
    s = input()
    
    result = timeConversion(s)
    
    f.write(result + '\n')
    
    f.close()

