class Solution:
    def __init__(self):
        self.lis = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        def find(nums,ind,l):
            if(ind<l):
                for i in range(l):
                    nums[ind],nums[i] = nums[i],nums[ind]
                    k = nums[0:l]
                    if(k not in self.lis):
                        self.lis.append(k)
                    find(nums,ind+1,l)
                    nums[i],nums[ind] = nums[ind],nums[i]
        find(nums,0,len(nums))
        return self.lis