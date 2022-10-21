class Solution:
    def mostPoints(self, nums: List[List[int]]) -> int:
        l = len(nums)
        dp = [0]*l
        for i in range(l-1,-1,-1):
            points = nums[i][0]
            bp = nums[i][1]
            futureind = i+bp+1
            if(futureind<l):
                dp[i] = dp[futureind]+points 
            else:
                dp[i] = points
            if(i<l-1):
                dp[i] = max(dp[i+1],dp[i])
        return max(dp)