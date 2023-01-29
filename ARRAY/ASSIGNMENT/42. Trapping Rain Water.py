class Solution:
    def trap(self, height: List[int]) -> int:
        from_right = []
        l = len(height)
        one,two = [0]*l,[0]*l
        left = height[0]
        # first and last block can't store any water
        for i in range(1,l):
            one[i] = left 
            left = max(left,height[i])
        right = height[-1]
        for i in range(l-2,-1,-1):
            two[i] = right 
            right = max(right,height[i])
        print(one)
        print(two)
        print(height)
        ctr = 0
        for i in range(1,l-1):
            if(height[i]< one[i] and height[i]<two[i]):
                #at index 5 we have 0 at left max is 2 right max is 3
                #so water will be present till lower block here it is 2 which is left side so water will be till 2 in y axis so to find the unit so 2-0 = 2 unit of water
                mn = min(one[i],two[i]) # water can store till min height [5] [9] till 5 water will be present
                ctr+=mn-height[i] # get the area if [5] [2] [7] water level at 2 is 5-2 = 3
        return ctr
