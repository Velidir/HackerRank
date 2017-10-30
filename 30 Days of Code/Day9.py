#!/bin/python3

import sys

def factorial(n):
    s = 1
    if(n <= 1):
        return 1
    else:
        while(n >= 2):
            n, s = n-1,s*(n)
    return(s)


if __name__ == "__main__":
    n = int(input().strip())
    result = factorial(n)
    print(result)
