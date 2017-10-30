#!/bin/python3

import sys


n = int(input().strip())
bit=("{:b}".format(n))
lbit=list(bit)

if bit.find("1") != -1:
    count=1
    maxcount=1
    for i,val in enumerate(lbit):
            if val == '1' and lbit[i-1]==val and i > 0:
                count+=1
            else:
                if count > maxcount:
                    maxcount=count
                count=1
    if count > maxcount:
        maxcount = count
    print(maxcount)
else:
    print(0)
