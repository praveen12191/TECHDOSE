class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mn = max(weights)
        mx = sum(weights)
        while(mn<mx):
            mid = mn+(mx-mn)//2 
            day = 0
            w = 0 
            ctr = 0
            for i in weights:
                if(i+w > mid):
                    day+=1 
                    w = 0 
                w+=i 
            if(day>=days):
                mn = mid+1 
            else:
                mx = mid
        return mn
            
                    