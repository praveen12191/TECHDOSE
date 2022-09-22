def quick(lis,start,end,ele):
    if(start<end):
        p = end-1 
        i = start-1
        for j in range(start,end):
            if(j==p):
                lis[i+1],lis[p] = lis[p],lis[i+1]
                i+=1
            elif(lis[p]>=lis[j]):
                lis[i+1],lis[j] = lis[j],lis[i+1]
                i+=1
        print(lis)
        if(i==ele):
            print(lis[i],lis)
            return lis[i]
        if(ele<i):
            quick(lis,start,i,ele)
        else:
            quick(lis,i,end,ele)
lis = list(map(int,input().split()))
ele = int(input())
print(quick(lis,0,len(lis),ele))