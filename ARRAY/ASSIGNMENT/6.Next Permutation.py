class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)-1
        ptr = l
        ctr = 0
        while(ptr-1>=0 and nums[ptr]<=nums[ptr-1]):
            ptr-=1 
        print(ptr)
        if(ptr==0):
            nums[0:l+1] = nums[::-1]
            return nums
        ptr-=1 
        k = ptr
        for i in range(l,-1,-1):
            if(nums[ptr]<nums[i]):
                v = i 
                break 
        nums[k],nums[v] = nums[v],nums[k]
        val = nums[k+1:l+1]
        nums[k+1:l+1] = val[::-1]
        return nums