from math import sqrt
def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True


no=int(raw_input())

arr=[]

for i in range(0,no):
    arr.append(int(raw_input()))

for x in range(0,no):
    if(prime(arr[x])):
        print "Prime"
    else:
        print "Not prime"
