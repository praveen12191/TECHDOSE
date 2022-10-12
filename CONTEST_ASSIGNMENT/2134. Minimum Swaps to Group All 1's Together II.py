class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        arr = nums+nums
        mn = float('inf')
        ctr = arr.count(1)
        ctr2 = arr[0:ctr].count(0)
        mn = ctr2
        for i in range(ctr,n+n):
            if(arr[i]==0):
                ctr2+=1 
            if(arr[i-ctr]==0):
                ctr2-=1 
            mn = min(mn,ctr2)
        return mn
