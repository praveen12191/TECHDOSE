lis = list(map(int,input().split()))
l = len(lis)
mx = max(lis)
has = [0]*(mx+1)
ans = [0]*(l)
for i in lis:
    has[i]+=1 
for i in range(1,mx+1):
    has[i] = has[i]+has[i-1]
for i in lis[::-1]:
    has[i]-=1 
    ind = has[i]
    ans[ind] = i 
print(ans)