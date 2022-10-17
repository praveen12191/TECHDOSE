class Solution:
    def isValid(self, s: str) -> bool:
        lis = []
        if(len(s)<2):
            return 0
        f = 0 
        for i in s:
            if(i=='{' or i=='[' or i=='('):
                f = 1
                lis.append(i)
            else:
                if(len(lis)==0):
                    return 0
                if(i=='}' and lis[-1]=='{'):
                    lis.pop(-1)
                elif(i==']' and lis[-1]=='['):
                    lis.pop(-1)
                elif(i==')' and lis[-1]=='('):
                    lis.pop(-1)
                else:
                    return 0
        if(len(lis)==0):
            return 1
        return 0