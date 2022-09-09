def ones_com(n):
    return ~n      
def twos_com(n):
    k = ones_com(n)
    return k+1 
a = int(input())
print(ones_com(a))
print(twos_com(a))
print(bin(32))
s= "a"
print(ord(s)^32)