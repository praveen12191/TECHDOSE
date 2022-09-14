class Solution:
    def mySqrt(self, x: int) -> int:
        ctr = 1 
        while(ctr*ctr<=x):
            ctr+=1 
        return ctr-1