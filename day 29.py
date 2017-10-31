

import sys


t = int(raw_input())
for a0 in range(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]


    maxi=0
    for p in range(1,n):

        for q in range(p+1,n+1):


         new_max=p & q
         if k > new_max > maxi:
             maxi = new_max

    print maxi






