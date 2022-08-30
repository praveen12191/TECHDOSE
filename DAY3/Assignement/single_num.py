class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        val = 0 
        for i in range(l):
            val^=nums[i]
        return val