
#User function Template for python3

class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
        ctr1,ctr2 = 0,0
        if(arr1[0]<arr2[0]):
            f = 1
        while(ctr1<n and ctr2<m):
            if(arr1[ctr1]<arr2[ctr2]):
                ctr1+=1
            else:
                arr1[ctr1],arr2[ctr2] = arr2[ctr2],arr1[ctr1]
                ctr1+=1
                arr2.sort()
        return arr1
            
        


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n,m = map(int, input().strip().split())
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        ob=Solution()
        ob.merge(arr1, arr2, n, m)
        print(*arr1,end=" ")
        print(*arr2)
# } Driver Code Ends