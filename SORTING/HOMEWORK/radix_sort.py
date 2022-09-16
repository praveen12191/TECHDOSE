lis = list(map(int,input().split()))
mx1 = max(lis)
has = [0]*10
ctr = 0 
mx_dig = 0
while(mx1):
    ctr+=1 
    mx1//=10 
pos = 10
val = 1
for i in range(ctr):
    ans = [0]*len(lis)
    has = [0]*10
    for j in lis:
        print(has,j%pos)
        has[(j//val)%pos]+=1 
    cum = has 
    for j in range(1,10):
        cum[j] = cum[j]+cum[j-1]
    print(cum)
    for j in lis[::-1]:
        print((j//val)%pos)
        cum[(j//val)%pos]-=1
        ans[cum[(j//val)%pos]] = j
    for j in range(len(lis)):
        lis[j] =ans[j]
    val*=10
print(ans)
    
    
     
