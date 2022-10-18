class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        stack = []
        h.append(0) # for 2nd test case 
        l = len(h)
        mx = 0 
        for i in range(l):
            while(stack and h[stack[-1]]>=h[i]):
                height = h[stack.pop()] # taking the largest height 
                width = i if not stack else i - stack[-1] - 1 
                mx = max(mx,height*width)
            stack.append(i)
        return mx