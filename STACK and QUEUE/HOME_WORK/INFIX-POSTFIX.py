#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, exp):
        ans = ""
        has = {'+':1,'-':1,'*':2,'/':2,'^':4 ,'(':0,')':0}
        stack = []
        for i in exp:
            if(i in has):
                if(i=='('):
                    stack.append('(')
                    continue
                if(i==')'):
                    k = ""
                    while(stack and k!='('):
                        k = stack.pop()
                        if(k!='('):
                            ans+=k 
                    continue
                while(stack and has[stack[-1]]>=has[i] and stack[-1]!='('):
                    v = stack.pop()
                    ans+=v
                stack.append(i)
            else:
                ans+=i
        while(stack):
            ans+=stack.pop()
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)


_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        exp = str(input())
        ob=Solution()
        print(ob.InfixtoPostfix(exp))
# } Driver Code Ends