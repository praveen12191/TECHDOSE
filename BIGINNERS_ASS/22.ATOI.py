class Solution:
    def myAtoi(self, s: str) -> int:
        f = 0 
        sign = 1
        k = 0
        MIN = -2**31
        MAX = 2**31 -1
        for i in s:
            if(f==0):
                if(i==' '):
                    continue 
                elif(i=='-'):
                    sign = -1 
                elif(i=='+'):
                    sign = 1 
                elif(i.isdigit()):
                    k = int(i)
                else:
                    return 0 
                f = 1 
            else:
                if(i.isdigit()):
                    k = k*10 + int(i)
                else:
                    break 
        print(k)
        if(sign*k<MIN):
            return MIN
        elif(sign*k>MAX):
            return MAX
        else:
            return k*sign
        
                  