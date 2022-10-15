class Solution:
    def fillCups(self, a: List[int]) -> int:
        ctr = 0 
        a.sort()
        first = 2
        second = 1
        while(a[first]!=0 and a[second]!=0):
            a[first]-=1 
            a[second]-=1 
            ctr+=1 
            a.sort()
        while(a[first]!=0):
            ctr+=1 
            a[first]-=1
        return ctr
                
                    
                