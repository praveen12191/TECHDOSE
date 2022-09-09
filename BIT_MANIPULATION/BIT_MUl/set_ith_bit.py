def set_ith(n,pos):
    #0->1 
    n = n|1<<pos-1
    return n  
def un_set(n,pos):
    #1->0 
    n = n& ~(1<<pos-1)
    print(bin(n))
    return n 
n,pos = map(int,input().split())
print(set_ith(n,pos))
print(un_set(n,pos))