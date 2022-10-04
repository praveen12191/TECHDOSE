class Solution:
    def __init__(self):
        self.ans = []
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            k = -1*nums[i] 
            self.twosum(nums,k,i)
        self.ans.sort()
        return self.ans
    def twosum(self,nums,tar,ind):
        has = defaultdict(int)
        for i in range(ind+1,len(nums)):
            if(nums[i] in has):
                lis = [-1*tar,nums[i],nums[has[nums[i]]]]
                lis.sort()
                if(lis not in self.ans):
                    self.ans.append(lis)
                    lis = []
            else:
                has[tar-nums[i]]=i