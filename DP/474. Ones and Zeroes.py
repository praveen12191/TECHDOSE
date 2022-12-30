class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        ctr = 0 
        l,lis = len(strs),[]
        dp = {}
        for i in strs:
            z,o = 0,0
            for j in i:
                if(j=='0'):
                    z+=1 
                if(j=='1'):
                    o+=1
            lis.append([z,o])
        def find(ind,zero,one):
            if(ind==l or zero<0 or one<0):
                return 0 
            if((zero,one,ind) in dp):
                return dp[zero,one,ind]
            z,o = lis[ind]
            exclude = find(ind+1,zero,one)
            include = 0
            if(zero-z>=0 and one-o>=0):
                include = 1+find(ind+1,zero-z,one-o)
            res = max(include,exclude)
            dp[zero,one,ind] = res
            return res
        return find(0,m,n)
