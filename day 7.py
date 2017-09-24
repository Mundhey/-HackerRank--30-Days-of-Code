#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(str,raw_input().strip().split(' '))

arr.reverse()
abc = ' '.join(arr)
print abc