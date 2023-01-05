class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        r = len(grid)
        c = len(grid[0])
        lis = [[0]*(c*3) for i in range(r*3)]
        for i in range(r):
            for j in range(c):
                ch = grid[i][j]
                if(ch=="/"):
                    lis[i*3][j*3 + 2] = 1 
                    lis[i*3 +1][j*3 + 1] = 1
                    lis[i*3 +2][j*3] = 1
                elif(ch=="\\"):
                    lis[i*3][j*3] = 1
                    lis[i*3 + 1][j*3 + 1] = 1
                    lis[i*3 + 2][j*3 + 2] = 1 
        ctr = 0
        for i in range(r*3):
            for j in range(c*3):
                if(lis[i][j]==0):
                    ctr+=1 
                    que = [[i,j]]
                    while(que):
                        row,col = que.pop(0)
                        if(lis[row][col]==1):
                            continue
                        lis[row][col] = 1 
                        for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                            ro = x+row
                            cl = y+col
                            if(ro>=0 and ro<r*3 and cl>=0 and cl<c*3):
                                if(lis[ro][cl]==0):
                                    que.append([ro,cl])
        return ctr
                        
