class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        [2,9,7,8,3,4,6,1]
         0 1 2 3 4 5 6 7
        
        if [3] is min so substring are till small ele than 3 on left 
        and small ell less than 3 on right side 
        2 -> left and right->1 
        so from 1 to 6 min ele is 3 
        978346,97834,9783,783,.... totaly 12 possible 
        ans => 2... 3 and 3...1 
               0    4     4   7 
        ind1 = number of element from left of 3 not include 2 ->3
        ind2 = number of element from right of 3 not include 1 ->2 
        so 3 * (ind1+1)*(ind2+1)
        if there is no small element 
        eg: 9 7 8 3 
            0 1 2 3 
        ind1 = number of element from left -> 3  
        '''
        l = len(arr)
        pre = []
        next = []
        mod = 10**9 + 7
        for i in range(l):
            # if there is no element smaller than 3
            pre.append(i)
            next.append(l-i-1)
        lis,lis2 = [],[]
        for i in range(l-1,-1,-1):
            while(len(lis)!=0 and arr[lis[-1]]>=arr[i]):
                k = lis.pop()
                pre[k] = k-i-1
            lis.append(i)
        print(pre)
        for i in range(l):
            while(len(lis2)!=0 and arr[lis2[-1]]>arr[i]):
                k = lis2.pop()
                next[k] = i-k-1
            lis2.append(i)
        print(next)
        sm = 0
        an = 0
        for i in range(l):
            an+=arr[i]*((pre[i]+1)*(next[i]+1))
        return an%mod