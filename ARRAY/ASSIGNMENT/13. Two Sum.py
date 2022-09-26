class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        l = len(nums)
        for i in range(l):
            if(nums[i] in dic):
                return [dic[nums[i]],i]
            else:
                dic[target-nums[i]] = i 

            