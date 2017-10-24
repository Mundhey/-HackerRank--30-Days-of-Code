#!/bin/python

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
totalswaps=0


for i in range(0,n,1):

    numberOfSwaps = 0


    for j in range(0,n-1,1):

        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            numberOfSwaps=numberOfSwaps+1
            totalswaps=totalswaps+1

    if numberOfSwaps==0:
        break



print "Array is sorted in %d swaps."% totalswaps
print "First Element: %d"%a[0]
print "Last Element: %d"%a[n-1]