lis = list(map(int,input().split()))
ans = []
for i in lis:
    ans.append(i)
    l = len(ans)
    for j in range(l-1,0,-1):
        if(ans[j]<=ans[j-1]):
            ans[j],ans[j-1] = ans[j-1],ans[j]
        else:
            break
print(ans)
