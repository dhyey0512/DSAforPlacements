

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    l = [[] for _ in range(n)]
    result = []
    lastanswer = 0

    for i in queries:
        a = (lastanswer ^ i[1]) % n

        if i[0] == 1:
            l[a].append(i[2])
        elif i[0] == 2:
            a = (lastanswer ^ i[1]) % n
            lastanswer = l[a][i[2] % len(l[a])]
            result.append(lastanswer)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
