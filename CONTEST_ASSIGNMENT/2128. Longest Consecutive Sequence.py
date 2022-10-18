class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        mx = 0 
        ctr = 0 
        l = len(nums)
        if(l==0):
            return 0
        for i in range(l-1):
            if(nums[i+1]==nums[i]):
                continue
            if(nums[i+1]-nums[i]==1):
                ctr+=1 
            else:
                mx = max(ctr,mx)
                ctr = 0
        mx = max(ctr,mx)
        return mx+1