class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2)+1)] for i in range(len(text1)+1)]
        '''
        def find(x,y):
            if(dp[x][y]!=-1):
                return dp[x][y]
            if(x==0 or y==0):
                return 0 
            if(text1[x-1]==text2[y-1]):
                return 1+find(x-1,y-1)
            dp[x][y] = max(find(x-1,y),find(x,y-1))
            return dp[x][y]
        return find(len(text1),len(text2))
        '''
        for i in range(len(text1)+1):
            for j in range(len(text2)+1):
                if(i==0 or j==0):
                    continue 
                if(text1[i-1]==text2[j-1]):
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        l1,l2 = len(text1),len(text2)
        def find(l1,l2):
            if(l1==0 or l2==0):
                return 
            if(text1[l1-1]==text2[l2-1]):
                self.ans+=text1[l1-1]
                find(l1-1,l2-1)
            else:
                if(dp[l1-1][l2]<=dp[l1][l2-1]):
                    find(l1,l2-1)
                else:
                    find(l1-1,l2)
        self.ans = ""
        find(l1,l2)
        print(self.ans)

        return dp[l1][l2]






