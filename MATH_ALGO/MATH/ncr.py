n = int(input())
ctr = 1 
lis = []
for i in range(n+1):
    l = []
    for j in range(ctr):
        l.append(0)
    ctr+=1 
    lis.append(l)
for i in range(n+1):
    print(lis[i])
ctr = 1 
for i in range(n+1):
    for j in range(ctr):
        if(j==0 or i==j):
            lis[i][j] = 1 
        else:
            lis[i][j] = lis[i-1][j]+lis[i-1][j-1]
    ctr+=1
for i in range(n+1):
    print(lis[i])