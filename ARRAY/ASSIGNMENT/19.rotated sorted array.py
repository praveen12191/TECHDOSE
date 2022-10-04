class Solution:
    def search(self, nums: List[int], t: int) -> int:
        if(t not in nums):
            return -1 
        ans = nums[t::]+nums[0:t]
        for i in range(len(nums)):
            if(nums[i]==t):
                return i