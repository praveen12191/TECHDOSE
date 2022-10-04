class Solution: 
    def __init__(self):
        self.ans = []
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        for i in range(len(nums)):
            self.threeSum(nums,i,target-nums[i],target,nums[i])
        self.ans.sort()
        return self.ans
    def threeSum(self,nums,ind,tar,total,st):
        for i in range(ind+1,len(nums)):
            self.twosum(nums,st,nums[i],tar-nums[i],i)
        return self.ans
    def twosum(self,nums,st,tr,tar,ind):
        has = defaultdict(int)
        for i in range(ind+1,len(nums)):
            if(nums[i] in has):
                lis = [st,tr,nums[has[nums[i]]],nums[i]]
                lis.sort()
                if(lis not in self.ans):
                    self.ans.append(lis)
                lis = []
            else:
                has[tar-nums[i]]=i