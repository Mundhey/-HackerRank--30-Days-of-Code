N=int(raw_input())
x="{0:b}".format(N)

count=0
num=[]
for i in range(0,len(x)):

    if(x[i]=='1'):
        count+=1
        if(len(x)==count):
            print count
            exit(0)
        if(i+1==len(x)):
            num.append(count)
    elif(x[i]=='0'):
        num.append(count)
        count=0




print max(num)

