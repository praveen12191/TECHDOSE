n = int(input())
lis = [0]*(n+1)
i = 2 
while(i*i<=n):
    if(lis[i]==0):
        j = 2
        while(i*j<=n):
            lis[j*i] = 1 
            j+=1
    i+=1 
print(lis)
print(lis.count(0)-2)