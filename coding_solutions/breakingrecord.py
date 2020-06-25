import math
import os
import random
import re
import sys
def breakingRecords(scores):
    max=scores[0]
    wr=0
    wm=0
    min=scores[0]
    for i in range(len(scores)):
        if max<scores[i]:
            max=scores[i]
            wr=wr+1
        if min>scores[i]:
            min=scores[i]
            wm=wm+1
    return wr,wm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
