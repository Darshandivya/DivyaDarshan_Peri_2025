# Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers, the one whose digits sum to a larger number is better than the other. If the sum of digits is equal for both numbers, then she thinks the smaller number is better. For example, Kristen thinks that  is better than  and that  is better than .

# Given an integer, , can you find the divisor of  that Kristin will consider to be the best?

# Input Format

# A single integer denoting .

# Constraints

# Output Format

# Print an integer denoting the best divisor of .

# Sample Input 0

# 12
# Sample Output 0

# 6
# Explanation 0

# The set of divisors of  can be expressed as . The divisor whose digits sum to the largest number is  (
    #!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    temp = []
    for i in range(1,n+1):
        if n % i == 0:
            temp.append(i)
    res = []
    for ele in temp:
        sum = 0
        for digit in str(ele):
            sum += int(digit)
        res.append(sum)
    val = max(res)
    index = res.index(val)
    print(temp[index])