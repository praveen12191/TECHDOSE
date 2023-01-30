class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        '''
        m = 3 and n = 3 and k = 6 
        1  2  3 -> (1)
        2  4  6 -> (2)
        3  6  9 -> (3)
        find ctr position for 4
        (1)  (4//1) = 4 mean [1,2,3,4] at 4th pos so for 4 we have 3 ele before = 3
        (2)  (4//2) = 2 mean [2,4] here 4 at 2nd pos so before 4 [2,4] = 2
        (3)  (4//3) = 1 ...
        '''
        def find(val):
            num = 0 
            for i in range(1,m+1):
                k1 = min(val//i,n) #min of col or ele before it 
                num+=k1
            return num
        start,end = 1,m*n 
        while(start<=end):
            mid = (end+start)//2
            v = find(mid)
            if(v<k):
                start = mid+1
            else:
                end = mid-1
        print(4//3)
        return start