class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        lis = [1]*l 
        ctr = [1]*l 
        mx = 1
        for i in range(1,l):
            for j in range(0,i):
                if(nums[i]>nums[j] and lis[i]<=lis[j]):
                    lis[i] = lis[j]+1 
                    mx = max(mx,lis[i])
                    ctr[i] = ctr[j]
                elif(nums[i]>nums[j] and lis[i]==lis[j]+1):
                    ctr[i]+=ctr[j]
        count = 0
        for i in range(l):
            if(lis[i]==mx):
                count+=ctr[i]
        return count

        
