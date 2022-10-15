class Solution:
    def maximumGroups(self, nums: List[int]) -> int:
        l = len(nums)
        ctr = 1
        i = 0
        nums.sort()
        ptr,count = 0,0
        k,lis = [],[]
        for i in nums:
            ptr+=1 
            if(ptr==ctr):
                count+=1
                ptr=0
                ctr+=1 
        return count