# Enter your code here. Read input from STDIN. Print output to STDOUT

N=int(raw_input())

for i in range(0,N):
    abc=(raw_input().strip(''))


    for x in range(0,len(abc),2):
        print abc[x],
    print "",
    for x in range(1,len(abc),2):
        print abc[x],
    print ""