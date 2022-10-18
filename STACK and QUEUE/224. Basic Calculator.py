class Solution:
    def calculate(self, s: str) -> int:
        num,sign = 0,1
        stack = []
        res = 0
        for i in s:
            if(i.isdigit()):
                k = int(i)
                num = num*10 + k 
            elif(i=='+'):
                res += num*sign
                num = 0 
                sign = 1 
            elif(i=='-'):
                res += (num*sign)
                num = 0 
                sign = -1
            elif(i=='('):
                stack.append(res)
                stack.append(sign)
                res = 0 
                sign = 1 
            elif(i==')'):
                res += num*sign
                num = 0 
                res *= stack.pop()
                res += stack.pop()
        res += num*sign
        return res