class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        start = 0 
        end = len(nums)
        ans,ctr = 0,0 
        while(start<end):
            if(nums[start]==0):
                ctr+=1 
                ans+=ctr 
            else:
                ctr = 0
            start+=1
        return ans