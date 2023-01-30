#User function Template for python3
from bisect import bisect_right
class Solution:
    def median(self, matrix, R, C):
        mn = matrix[0][0]
        mx = 0 
        for i in range(R):
            mn = min(mn,matrix[i][0])
            mx = max(mx,matrix[i][C-1])
        medd = ((R*C)+1)//2
        while(mn<mx):
            mid = (mn+mx)//2
            left = 0 
            for i in range(R):
                left+=bisect_right(matrix[i],mid)
            if(left<medd):
                mn = mid+1
            else:
                mx = mid
        return mn


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)
# } Driver Code Ends