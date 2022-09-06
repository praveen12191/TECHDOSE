n = int(input())
i = 2
while(i*i<=n):
    val = n/i 
    if(val*val == n):
        print("Yes")
        break 
    i+=1
else:
    print("No")