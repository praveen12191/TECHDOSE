a = int(input())
b = int(input())
c = 1 
while(b>0):
    if(b%2==1):
        c*=a     
    a=a*a    
    b = b//2 
print(c)
    