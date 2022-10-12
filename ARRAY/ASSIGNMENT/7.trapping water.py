class Solution:
    def trap(self, height: List[int]) -> int:
        from_right = []
        l = len(height)
        one,two = [0]*l,[0]*l
        left = height[0]
        for i in range(1,l):
            one[i] = left 
            left = max(left,height[i])
        right = height[-1]
        for i in range(l-2,-1,-1):
            two[i] = right 
            right = max(right,height[i])
        print(one)
        print(two)
        ctr = 0
        for i in range(1,l-1):
            if(height[i]< one[i] and height[i]<two[i]):
                mn = min(one[i],two[i])
                ctr+=mn-height[i]
        return ctr
