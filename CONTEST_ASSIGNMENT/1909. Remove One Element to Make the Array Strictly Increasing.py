class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        l = len(nums)
        ind,ctr = 0,0
        for i in range(l-1):
            if(nums[i]>=nums[i+1]):
                ctr+=1 
                ind = i
        if(ctr==0):
            return 1
        if(ctr==1):
            if(ind==0 or ind==l-2):
                return 1 
            if(nums[ind-1]<nums[ind+1] or nums[ind]<nums[ind+2]):
                return 1
        return 0