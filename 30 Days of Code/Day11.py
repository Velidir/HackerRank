#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

sums=[]
for i in range(len(arr)-2):
    for j in range(len(arr[i])-2):
        item1 = arr[i][j]
        item2 = arr[i][j+1]
        item3 = arr[i][j+2]
        item4 = arr[i+1][j+1]
        item5 = arr[i+2][j]
        item6 = arr[i + 2][j+1]
        item7 = arr[i + 2][j +2]
        sums.append(item1+item2+item3+item4+item5+item6+item7)


        # print(item1,item2,item3)
        # print(" ",item4," ")
        # print(item5,item6,item7)
print(max(sums))