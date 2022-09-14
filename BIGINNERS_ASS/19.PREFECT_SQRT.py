n = int(input())
ctr = 2 
while(ctr*ctr<=n):
    if(ctr*ctr==n):
        print("YES")
        break 
    ctr+=1 
else:
    print("NO")