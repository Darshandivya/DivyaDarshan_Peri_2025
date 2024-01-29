# #!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ampm = s[-2:]
    s = s[:len(s)-2]
    hh, mm, ss = s.split(':')
    if ampm == 'AM' and hh == '12':
        hh = '00'
    elif ampm == 'PM' and hh != '12':
        hh = str(int(hh)+12)
    return hh+":"+mm+":"+ss
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
