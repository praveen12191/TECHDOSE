class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''  3open and 3close 
             close should not grater than open '())' so close<open
             if open == close ad to result 
        1. ["("] open = 1 
        open < n and close<open so we have two way 
        one add open ["(("] or add close ["()"]
        2. ["(("]                        ["()"]
…        return res
             |
             |
        open<n and close<open 
        so ["((("] and ["(()"]  ...'''
        stack = []
        res = []
        def back(open,close):
            if(open==close==n):
                res.append(''.join(stack))
                return 