#!/bin/python3

import sys

y = input().strip()
n = int(y)
for i in range(1, 11):
    count = str(i)
    print(y + " x " + count + " = " + str(n * i))
