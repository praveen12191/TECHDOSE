lis= list(map(int,input().split()))
l = len(lis)
for i in range(l-1,-1,-1):
    no_swap=1
    for j in range(0,i):
        if(lis[j]>lis[j+1]):
            no_swap = 0
            lis[j+1],lis[j] = lis[j],lis[j+1]
    if(no_swap):# if there no swap then the lis is sorted so break it 
        break
print(lis)