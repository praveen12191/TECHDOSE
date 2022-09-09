n = int(input())
for i in range(2,n/2):
    if(n%i==0):
        print("No")
        break 
else:
    print("Yes")
    