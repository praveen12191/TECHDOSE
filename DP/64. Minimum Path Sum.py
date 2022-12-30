class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        l1 = len(grid)
        l2 = len(grid[0])
        #bfs
        # vis = [[0 for i in range(l2)] for i in range(l1)]
        # dis = [[0,-1],[-1,0],[1,0],[0,1]]
        # qe = [[0,0,grid[0][0],[[0,0]]]]
        # mn = float('inf')
        # while(qe):
        #     r,c,sm,val = qe.pop(0)
        #     vis[r][c] = 1
        #     for row,col in dis:
        #         x,y = r+row,c+col
        #         if(x==l1-1 and y==l2-1):
        #             mn = min(mn,sm+grid[l1-1][l2-1])
        #         if(x>=0 and x<l1 and y>=0 and y<l2 and vis[x][y]==0):
        #             qe.append([x,y,sm+grid[x][y],[[x,y]]+val])
        # if(len(grid)==1 and len(grid[0])==1):
        #     if(grid[0][0]==0):
        #         return 0 
        #     return grid[0][0]
        # return mn
        dp = [[-1 for i in range(l2)] for i in range(l1)]
        def dfs(l1,l2):
            if(l1==0 and l2==0):
                return grid[0][0]
            if(dp[l1][l2]!=-1):
                return dp[l1][l2]
            if(l1==0):
                return grid[0][l2]+dfs(l1,l2-1)
            if(l2==0):
                return grid[l1][l2]+dfs(l1-1,l2)
            dp[l1][l2] = grid[l1][l2]+min(dfs(l1-1,l2),dfs(l1,l2-1))
            return dp[l1][l2]
        k = dfs(l1-1,l2-1)
        print(dp)
        return k