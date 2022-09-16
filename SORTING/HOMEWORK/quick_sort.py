def quick_sort(lis,start,end):
    if(start<end):
        p = end-1 
        i = start-1
        for j in range(start,end):
            if(j==p):
                lis[i+1],lis[p] = lis[p],lis[i+1]
                i+=1
            elif(lis[j]<=lis[p]):
                i+=1 
                lis[i],lis[j] = lis[j],lis[i]
        quick_sort(lis,start,i)
        quick_sort(lis,i+1,end)

lis = [1,6,2,10,5]
i = -1 
p = 4
quick_sort(lis,0,5)
print(lis)