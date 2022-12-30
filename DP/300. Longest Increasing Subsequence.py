class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        # lis = [[-1 for i in range(l+1)] for i in range(l+1)]
        # def find(ctr_ind,pre_ind):
        #     if(ctr_ind==l):
        #         return 0 
        #     if(lis[ctr_ind][pre_ind+1]!=-1):
        #         return lis[ctr_ind][pre_ind+1]
        #     ln = 0+find(ctr_ind+1,pre_ind) # not include
        #     if(pre_ind==-1 or nums[pre_ind]<nums[ctr_ind]):
        #         ln = max(ln,1+find(ctr_ind+1,ctr_ind))
        #     lis[ctr_ind][pre_ind+1] = ln
        #     return lis[ctr_ind][pre_ind+1]
        # return find(0,-1)
        lis = [1]*l 
        mx = 1
        for i in range(1,l):
            for j in range(0,i):
                if(nums[i]>nums[j] and lis[j]>=lis[i]):
                    lis[i] = lis[j]+1 
                    mx = max(lis[i],mx)
        print(lis)
        return mx