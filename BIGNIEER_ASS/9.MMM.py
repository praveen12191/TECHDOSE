def median(lis):
    l = len(lis)
    if(l%2):
        print(lis[l//2])
    else:
        print(lis[l//2 - 1],lis[l//2])
def mean(lis):
    s = 0 
    for i in lis:
        s+=i 
    print(s)
def mode(lis):
    l = len(lis)
    map = {}
    for i in lis:
        map[i] = 0 
    for i in lis:
        map[i]+=1 
    mx = 0 
    for i,j in map.items():
        if(j>mx):
            mx = j 
    for i,j in map.items():
        if(j==mx):
            print(i,end=" ")
lis = list(map(int,input().split()))
median(lis)
mean(lis)
mode(lis)