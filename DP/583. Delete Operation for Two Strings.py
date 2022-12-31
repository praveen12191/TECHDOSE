class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1,l2 = len(word1),len(word2)
        if(word1==word2):
            return 0
        # has = {}
        # def find(l1,l2):
        #     if(l1==0): s1="" s2 ="ab" so 2 op to make s1 to s2
        #         return l2
        #     if(l2==0):
        #         return l1
        #     if((l1,l2) in has):
        #         return has[(l1,l2)]
        #     if(word1[l1-1]==word2[l2-1]):
        #         return find(l1-1,l2-1)
        #     k =  1+min(find(l1-1,l2),find(l1,l2-1))
        #     # s1 = abcd s2 aber
        #     # (l1-1,l2) s1 = abc s2 = aber 
        #     # (l1,l2-1) s1 = abcd s2 = aber
        #     has[(l1,l2)] = k 
        #     return k
        # return find(l1,l2)
        dp = [[0]*(l2+1) for i in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if(i==0 or j==0):
                    continue 
                if(word1[i-1]==word2[j-1]):
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        #find LCS and sub from the length
        return l1+l2 - 2*dp[l1][l2]