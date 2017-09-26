N=int(raw_input())

hashtable={}

for i in range(0,N):
    key,value=arr = map(str,raw_input().strip().split(' '))
    hashtable[key]=value


acc = []
out = ''
while True:
    try:
        acc.append(raw_input())
    except EOFError:
        break



XYZ=[]

for i in range(0,len(acc)):

    abc=hashtable.get(acc[i],"Not Found")
    if(abc=="Not Found"):
     XYZ.append("Not found")
    else:
     XYZ.append(acc[i]+"="+abc)

for i in range(0,len(XYZ)):
    print XYZ[i]