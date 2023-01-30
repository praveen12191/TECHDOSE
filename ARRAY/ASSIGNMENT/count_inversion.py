class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr1, n):
        self.inv = 0 
        def meg_sort(arr,l):
            if(l==1):
                return 
            mid = l//2
            arr1 = arr[0:mid]
            arr2 = arr[mid:]
            meg_sort(arr1,mid)
            meg_sort(arr2,l-mid)
            merge(arr1,arr2,arr)
        def merge(left,right,mid):
            ctr1,ctr2 = 0,0
            ptr = 0 
            while(ctr1<len(left) and ctr2<len(right)):
                if(left[ctr1]<=right[ctr2]):
                    mid[ptr] = left[ctr1]
                    ctr1+=1
                else:
                    self.inv+= len(left)-ctr1
                    mid[ptr] = right[ctr2]
                    ctr2+=1
                ptr+=1
            while(ctr1<len(left)):
                mid[ptr] = left[ctr1]
                ctr1+=1
                ptr+=1
            while(ctr2<len(right)):
                mid[ptr] = right[ctr2]
                ctr2+=1
                ptr+=1
            
        meg_sort(arr1,n)
        return self.inv
                    


                    





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends