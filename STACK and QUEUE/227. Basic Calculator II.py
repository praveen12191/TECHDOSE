class Solution:
    def calculate(self, s: str) -> int:
        sign,num = "+",0 
        res = 0 
        s+=' '
        stack = []
        for i in range(len(s)):
            if(s[i].isdigit()):
                num = num*10 + int(s[i])
            elif(s[i] in "+-/*" or i==len(s)-1):
                if(sign=='+'):
                    stack.append(num)
                elif(sign=='-'):
                    print(num)
                    stack.append(-num)
                elif(sign=='*'):
                    k = stack.pop()
                    stack.append(k*num)
                elif(sign=='/'):
                    k = stack.pop()
                    f = 0
                    if(k<0):
                        f = 1 
                        k = -k 
                    r = k//num
                    if(num==0):
                        stack.append(k)
                    elif(f):
                        stack.append(-r)
                    else:
                        stack.append(r)

                sign = s[i]
                num = 0 
            res = 0
        print(stack,num,sign)
        for i in stack:
            res+=i 
        return res
                