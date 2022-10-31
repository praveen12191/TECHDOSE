class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        has = {}
        mx,count=0,0
        l = len(nums)
        for i in range(l):
            count+= 1 if(nums[i]==1) else -1
            if(count==0):
                mx = max(mx,i+1)
            elif(count in has):
                mx = max(mx, i-has[count])
            else:
                has[count] = i
        return mx
    '''
    eg 0 1 1 0 1 1 
    in 0 1 2 3 4 5 
    1.count = -1 -> -1:0 
    2.count = 0 -> mx = i+1 
    3.count = 1 > -1:0 , 1:2 
    4.count = 0 -> mx = i+1
    5.count = 1 , we already have 1 in has so index is 1:2 ind=2 so from 
    ind 2 to ind 3 we have equal 
    
    '''