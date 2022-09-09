def set_bit(n):
    ctr=0
    while(n):
        if(n&1):
            ctr+=1 
        n=n>>1 
    return ctr
def set_bit_2(n):
    ctr = 0 
    i = 1 
    while(i<n):
        if(n&i):
            ctr+=1 
        i=1<<i 
    return ctr
n = int(input())
print(set_bit(n))
print(set_bit_2(n))