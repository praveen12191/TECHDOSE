class Solution:
    def climbStairs(self, n: int) -> int:
        lis = [-1]*(n+1)
        def find(n):
            if(n<3):
                return n 
            if(lis[n]!=-1):
                return lis[n]
            lis[n] = find(n-1)+find(n-2)
            return lis[n]
        return find(n)
        