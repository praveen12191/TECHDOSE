class Solution:
    def productQueries(self, n: int, q: List[List[int]]) -> List[int]:
        lis = []
        for i in range(33):
            if(n & 1<<i):
                lis.append(1<<i)
        pref = [lis[0]]
        for i in lis[1::]:
            pref.append(pref[-1]*i)
        res = []
        mod = 10**9 + 7
        for i,j in q:
            if(i==0):
                res.append(pref[j]%mod)
            else:
                res.append((pref[j]//pref[i-1])%mod)
        return res