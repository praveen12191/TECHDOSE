class Solution:
    def countBits(self, n: int) -> List[int]:
        lis = []
        for i in range(n+1):
            lis.append(self.countonce(i))
        return lis
    def countonce(self,val):
        ctr = 0
        for i in range(33):
            if(val&1<<i):
                ctr+=1 
        return ctr