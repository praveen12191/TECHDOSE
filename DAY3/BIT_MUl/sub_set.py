a = list(map(str,input().split()))
l = len(a)
lis= []
for i in range(2**l):
    s = []
    for j in range(l):
        if(i&(i<<j)):
            s.append(a[j])
    lis.append(s)
print(lis)