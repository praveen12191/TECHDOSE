class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = nums[0]
        l = len(nums)
        mx = nums[0]
        s = 0
        for i in range(l):
            s+=nums[i]
            if(mx<s):
                mx = s 
            if(s<0):
                s = 0 
                
        return mx