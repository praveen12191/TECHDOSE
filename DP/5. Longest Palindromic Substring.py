class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        dp = [[0 for i in range(l)] for i in range(l)]
        # for len 1 always palindrom
        for i in range(l):
            dp[i][i] = 1
        # for len 2 
        self.mx = 0 
        self.ind = 0 
        for i in range(l):
            if(i+1<l):
                if(s[i]==s[i+1]):
                    dp[i][i+1] = 1 
                    self.mx = i+1
                    self.ind = i
        def find(r,c):
            if(r>=l or c>=l):
                return 
            elif(s[r]==s[c] and dp[r+1][c-1]==1):
                dp[r][c] = 1 
                self.mx = c 
                self.ind = r 
            else:
                dp[r][c] = 0 
            find(r+1,c+1)
        for i in range(2,l):
            find(0,i)
        return s[self.ind:self.mx+1]
        



        
