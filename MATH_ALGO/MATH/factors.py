n = int(input())
i = 1 
while(i*i<=n):
    if(i*(n/i)==n):
        print(i,n/i)
    i+=1 