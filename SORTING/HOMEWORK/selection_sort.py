lis = list(map(int,input().split()))
l = len(lis)
for i in range(l-1):
    min_ind = i 
    for j in range(i+1,l):
        if(lis[min_ind]>lis[j]):
            min_ind = j 
    k = lis[min_ind]
    lis[min_ind] = lis[i]
    lis[i] = k 
print(lis)