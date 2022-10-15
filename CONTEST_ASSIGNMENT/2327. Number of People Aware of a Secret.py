class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        lis = [[delay+1,forget+1,1]]
        ctr = 2
        mod = 10**9 + 7 
        for i in range(2,n+1):
            for j in range(len(lis)):
                if(lis[j]!=[0] and lis[j][1]==i):
                    lis[j] = [0]
            ctr = 0
            for x in lis:
                if(x!=[0] and x[0]<=i):
                    ctr+=x[2]
            lis.append([delay+i,forget+i,ctr])
        ans = 0 
        for i in lis:
            if(i!=[0]):
                ans+=i[2]
        return ans%mod