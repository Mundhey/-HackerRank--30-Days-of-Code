#!/bin/python

import sys


n = int(raw_input().strip())

for i in range(1,11):
    print "%dx%d=%d"%(n,i,n*i)