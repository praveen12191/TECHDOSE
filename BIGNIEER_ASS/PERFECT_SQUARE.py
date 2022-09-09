n = int(input())
i = 2 
while(i*i<=n):
    if(i*i==n):
        print("YEs")
        break
    i+=1
else:
    print("No")