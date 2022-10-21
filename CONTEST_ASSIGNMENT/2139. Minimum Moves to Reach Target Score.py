class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        x = target
        f = 0
        ctr = 0
        while(target and maxDoubles):
            if(target%2==1):
                target-=1 
                ctr+=1
            else:
                target//=2 
                maxDoubles-=1
                ctr+=1
        return target+ctr -1