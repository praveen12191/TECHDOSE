def pow_of_2(n):
    return n&(n-1)
n = int(input())
if(pow_of_2(n)==0):
    print("YES")
else:
    print("No")