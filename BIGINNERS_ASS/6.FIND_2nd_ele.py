lis = list(map(int,input().split()))
l = len(lis)
first = 0 
sed = 0 
for i in lis:
    if(i>first):
        second = first 
        first = i 
    if(second<i and i!=first):
        second = i 
print(second)