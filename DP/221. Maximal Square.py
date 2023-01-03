class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r,c = len(matrix),len(matrix[0])
        dp = [[0]*(c+1) for i in range(r+1)]
        mx = 0
        for i in range(r+1):
            for j in range(c+1):
                if(i==0 or j==0):
                    continue
                if(matrix[i-1][j-1]=="1"):
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    mx = max(mx,dp[i][j])
        return mx*mx
        