class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        l1,l2 = len(str1),len(str2)
        dp = [[0]*(l2+1) for i in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if(i==0 or j==0):
                    continue 
                if(str1[i-1]==str2[j-1]):
                    dp[i][j]+=dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        self.ans = ""
        def find(l1,l2):
            if(l1==0 or l2==0):
                return 
            if(str1[l1-1]==str2[l2-1]):
                self.ans+=str1[l1-1]
                find(l1-1,l2-1)
            else:
                if(dp[l1-1][l2]>=dp[l1][l2-1]):
                    find(l1-1,l2)
                else:
                    find(l1,l2-1)
        find(l1,l2)
        s = ""
        self.ans = self.ans[::-1]
        l = len(self.ans)
        ctr1,ctr2 = 0,0
        '''
        s1 = abac
        s2 = cab lca = ab 
        so total l = s1+s2-len(lca) = 5 
        adding lca char only once
        '''
        for i in self.ans:
            while(ctr1<l1 and str1[ctr1]!=i):
                s+=str1[ctr1]
                ctr1+=1
            while(ctr2<l2 and str2[ctr2]!=i):
                s+=str2[ctr2]
                ctr2+=1
            s+=i 
            ctr1+=1
            ctr2+=1
        s+=str1[ctr1:]+str2[ctr2:]
        return s

            