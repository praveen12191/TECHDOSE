class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        val = x^y 
        ctr = 0
        for i in range(33):
            if(val&1<<i):
                ctr+=1 
        return ctr