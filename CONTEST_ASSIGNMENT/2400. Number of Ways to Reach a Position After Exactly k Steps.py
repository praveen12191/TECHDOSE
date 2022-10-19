class Solution:
    def __init__(self):
        self.ctr = 0
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        has = defaultdict(dict)
        mod = 10**9 + 7
        def find(start,end,k):
            if(k==0):
                if(start==end):
                    return 1
                return 0
            if(k in has and start in has[k]):
                return has[k][start]
                
            has[k][start] = find(start+1,end,k-1) + find(start-1,end,k-1)
            return has[k][start]
        return find(startPos,endPos,k)%mod