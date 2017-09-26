def factorial(N):


    if(N==1):
        return 1
    else:
        return N * factorial(N-1)







N=int(raw_input())

ans=factorial(N)
print ans