class Solution:
    def countEven(self, num: int) -> int:
        ctr = 0 
        for i in range(1,num+1):
            sm = 0 
            while(i):
                sm+=i%10 
                i//=10 
            if(sm%2==0):
                ctr+=1 
        return ctr