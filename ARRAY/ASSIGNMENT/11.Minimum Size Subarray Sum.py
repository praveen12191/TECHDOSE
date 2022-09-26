class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0 
        mx = len(nums)
        end = 0 
        sm = 0
        f = 0
        mn = float('inf')
        while(start<mx):
            sm+=nums[start]
            start+=1
            while(sm>=target and end<start):
                f = 1
                mn = min(mn,start-end)
                sm-=nums[end]
                end+=1
        if(f==0):
            return 0
        return mn