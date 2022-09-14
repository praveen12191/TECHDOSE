n = int(input())
lis = [0]*(n+1)
lis[0],lis[1] = 1,1 
for i in range(2,n+1):
    for j in range(0,i):
        lis[i] += lis[j]*lis[i-j-1]
print(lis)