a,b = map(int,input().split())
a = a^b     
b = b^a    
a = a^b     
print(a,b)