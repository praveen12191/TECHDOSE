class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        iterate to grid and store the index of the 2 with initial 0 time 
        0-> bzos initily we can take all 2 and performe the operation 
        eg [0,0] 
        after completion od [0,0] -> [0,1] and [1,0] become 2 and time will be 1
        .
        .
        .
        
        '''
        val = []
        lis = [[-1,0],[0,1],[1,0],[0,-1]]
        m = len(grid)
        n = len(grid[0])
        time = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):
                    val.append([0,[i,j]])
        while(val):
            k = val.pop(0)
            time = k[0]
            r = k[1][0]
            c = k[1][1]
            for x,y in lis:
                if(r+x>=0 and r+x<m and c+y>=0 and c+y<n and grid[x+r][y+c]==1):
                    grid[r+x][c+y] = 2 
                    val.append([time+1,[r+x,c+y]])
        for i in grid:
            if(1 in i):
                return -1 
        return time