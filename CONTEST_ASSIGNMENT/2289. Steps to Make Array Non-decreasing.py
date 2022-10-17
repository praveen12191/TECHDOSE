class Solution:
    def totalSteps(self, A: List[int]) -> int:
        l = len(A)
        stack = []
        dp = [0]*(l+1)
        for i in range(l-1,-1,-1):
            while(stack and A[stack[-1]]<A[i]):
                k = stack.pop()
                dp[i] = max(dp[i]+1,dp[k])
            stack.append(i)
        print(dp)
        return max(dp)