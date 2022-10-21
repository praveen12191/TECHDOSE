class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [[0 for i in range(n)] for j in range(m)]
        for i,j in guards:
            mat[i][j] = 'g'
        for i,j in walls:
            mat[i][j] = 'w'
        for i in mat:
            print(i)
        for i in range(m):
            for j in range(n):
                if(mat[i][j]=='g'):
                    if(j+1<n):
                        for x in range(j+1,n):
                            if(mat[i][x]=='g' or mat[i][x]=='w'):
                                break 
                            else:
                                mat[i][x] = 1 
                    if(i-1>=0):
                        for x in range(i-1,-1,-1):             
                            if(mat[x][j]=='g' or mat[x][j]=='w'):
                                break 
                            else:
                                mat[x][j] = 1
                    if(j-1<n):
                        for x in range(j-1,-1,-1):
                            if(mat[i][x]=='g' or mat[i][x]=='w'):
                                break 
                            else:
                                mat[i][x] = 1 
                    if(i+1<m):
                        for x in range(i+1,m):
                            if(mat[x][j]=='g' or mat[x][j]=='w'):
                                break 
                            else:
                                mat[x][j] = 1 
        ctr = 0
        for i in mat:
            ctr+=i.count(0)
        return ctr