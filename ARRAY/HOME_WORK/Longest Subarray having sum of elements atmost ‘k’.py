lis = [1,5,3,2,8,1,25]
k = 8
start = 0
l = len(lis)
sm = 0 
end = 0
while(start<l):
    sm+=lis[start]
    while(end<=start and sm>=k):
        if(sm==k):
            print(end,start)
        sm-=lis[end]
        end+=1
    start+=1