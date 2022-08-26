def o_or_e(a):
    return a&1 
a = int(input())
if(o_or_e(a)==0):
    print("EVEN")
else:
    print("ODD")