def right_most(n):
    ctr = 0
    while(n):
        ctr+=1
        if(n&1):
            return ctr
        n = n>>1
    return 0
n = int(input())
print(right_most(n))