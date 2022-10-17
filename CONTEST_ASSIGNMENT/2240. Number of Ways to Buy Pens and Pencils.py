class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        x = 0
        ans = 0
        while(1):
            k = cost1*x 
            t = total-k
            if(t<0):
                return ans
            ptr = (t//cost2)+1
            ans+=ptr
            x+=1