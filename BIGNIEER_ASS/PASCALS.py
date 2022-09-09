n = int(input())
lis = []
for i in range(1,n+1):
    k = [0]*i 
    lis.append(k)
for i in range(n):
    for j in range(i+1):
        if(i==j or j==0):
            lis[i][j] = 1 
        else:
            lis[i][j] = lis[i-1][j-1] + lis[i-1][j]
for i in lis:
    print(i)