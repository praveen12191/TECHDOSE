class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        eg 3 4 7 2 -3 1 4 2 
        pr 4 7 14 16 13 14 18 20  k = 7 
        property some = ctr_sum-k
        ctr_sum = some+k 
        and some where in ctr_sum we have [k] if it is 1 mean that one k if
        it is 2 then it has 2 k ...

        0:1 
        4 not in has so 4:1 
        7-7 is present so ctr = 1 0:1 ,4:1,7:1 [3,4]
        14-7 7 is present [7]
        16:1
        13:1
        14-7 is 7 so ctr = 3 [3,3][7][7,2,-1,1]
        eg 
        3 4  7  2 -3  1  4  2  1 
        3 7 14 16 13 14 18 20 21
        3:1
        7:1 
        14:2
        if(21-7) = 14 in has 14:2 ctr = 3 now ctr = 3+2 = 5 
        because [1,4,2] ans [4,2,1] we have 2 
        '''
        pref = [nums[0]]
        for i in nums[1::]:
            pref.append(pref[-1]+i)
        ctr = 0 
        has = {0:1}
        for i in pref:
            if(i-k in has):
                ctr+=has[i-k]
            if(i in has):
                has[i]+=1 
            else:
                has[i] = 1 
        return ctr
            
        