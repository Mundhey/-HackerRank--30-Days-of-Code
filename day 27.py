from __future__ import print_function
from random import randint
import random



t=5
print (t)
for i in range(1,t+1):
    n=randint(3,200)
    k=randint(1,n)

    for x in range (0,n):
        var = random.sample(range(-1000, 1000), n)
        var.sort()

    print (n,k)
    print(*var, sep=' ')

