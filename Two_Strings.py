'''
The link to the problem statement.
https://hackerrank-challenge-pdfs.s3.amazonaws.com/5187-two-strings-English?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1587324042&Signature=d4O0krpcemkAZQJMu%2BlSyoB272g%3D&response-content-disposition=inline%3B%20filename%3Dtwo-strings-English.pdf&response-content-type=application%2Fpdf
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    numOfOccurances = [0] * 26
    for i in s1:
        numOfOccurances[ord(i)-ord('a')] = True
    for i in s2:
        if(numOfOccurances[ord(i)-ord('a')] == True):
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
