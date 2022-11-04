class Solution:
    def __init__(self):
        self.mx = 0
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        height = [0]*(c+1)
        val = [0]*c
        ctr = 0 
        mx = 0 
        def find(val):
            stack = []
            val.append(0)
            mx = 0 
            for i in range(len(val)):
                while(stack and val[stack[-1]]>=val[i]):
                    height = val[stack.pop()]
                    width = i if not stack else i-stack[-1]-1
                    mx = max(mx,height*width)
                stack.append(i)
            return mx
        for i in range(r):
            for j in range(c):
                if(matrix[i][j]=="0"):
                    val[j] = 0 
                else:
                    val[j]+=int(matrix[i][j])
            mx = max(mx,find(val))
        return mx