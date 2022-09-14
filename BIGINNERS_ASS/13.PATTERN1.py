n = int(input())
k = n 
for i in range(n*2+1):
    if(i<=n):
        for j in range(1,i+1):
            print(j,end=" ")
        print()
    else:
        for j in range(k,0,-1):
            print(j,end=" ")
        k-=1
        print()