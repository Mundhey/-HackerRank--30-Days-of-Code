no=int(raw_input())

arr=[]

for i in range(0,no):
    arr.append(int(raw_input()))

for x in range(0,no):
    flag=1
    if(arr[x]==2):
        print "Prime"
        continue
    if(arr[x]==1):
        print "Not prime"
        continue

    for i in range(2,arr[x]-1):
        if arr[x] % i == 0:
            flag=0
            print "Not prime"
            break
    if(flag==1):
        print "Prime"

