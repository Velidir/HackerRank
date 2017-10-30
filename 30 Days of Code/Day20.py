#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0
sorted = False
while not sorted:
    sorted = True
    for i in range(len(a)-1):
        if (a[i] > a[i+1]):
            sorted = False
            a[i], a[i+1] = a[i+1], a[i]
            numSwaps = numSwaps + 1

print("Array is sorted in", numSwaps, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[len(a) - 1])


# Write Your Code Here
