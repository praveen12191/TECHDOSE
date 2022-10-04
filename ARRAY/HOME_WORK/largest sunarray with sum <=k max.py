lis = [2,4,5,6,7,1,2,3,1]
k = 7 
start,sm,end,mx = 0,0,0,0
l = len(lis)
end = 0
while(start<l):
    sm+=lis[start]
    while(end<=start and sm<k):
        print(sm,end,start)
        mx = max(mx,start-end +1)
        sm-=lis[end]
        end+=1 
    start+=1
print(mx)