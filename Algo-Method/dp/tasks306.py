#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    plusCount = 0
    minusCount = 0
    zeroCount = 0
    for i in range(n):
        if arr[i] < 0:
            minusCount += 1
        elif arr[i] > 0:
            plusCount += 1
        else:
            zeroCount += 1
    print(plusCount / n)
    print(minusCount / n)
    print(zeroCount / n)


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
