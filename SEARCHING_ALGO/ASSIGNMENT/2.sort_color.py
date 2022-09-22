class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        for i in range(l):
            ind = i 
            for j in range(i+1,l):
                if(nums[ind]>nums[j]):
                    ind = j 
            nums[ind],nums[i] = nums[i],nums[ind]
