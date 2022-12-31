class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lis = [[0 for x in range(n)] for x in range(m)]
        for x in range(m):
            for y in range(n):
                if(y==0 or x==0):
                    lis[x][y] = 1
                else:
                    lis[x][y] = lis[x][y-1]+lis[x-1][y] 
        print(lis)
        return lis[m-1][n-1]