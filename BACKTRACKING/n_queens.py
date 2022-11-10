class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        lis = [['.' for i in range(n)] for i in range(n)]
        pos_dig = set()
        neg_dig = set()
        ctr = set()
        ans = []
        def dfs(r):
            if(r==n):
                copy = [val for val in lis]
                ans.append(["".join(val) for val in copy])
            for c in range(n):
                if(c in ctr or c+r in pos_dig or r-c in neg_dig):
                    continue 
                ctr.add(c)
                pos_dig.add(c+r)
                neg_dig.add(r-c)
                lis[r][c] = 'Q'
                dfs(r+1)
                ctr.remove(c)
                pos_dig.remove(r+c)
                neg_dig.remove(r-c)
                lis[r][c] = '.'
        dfs(0)
        return ans
    '''
        0   1   2   
    0   .   .   .
    
    1   .   .   .
    
    2   .   .   .
    
    for positive dig (2,0),(1,1),(0,2) -> sum = 2 
    for postive dig  (1,0),(0,1)  -> sum = 1 
    row+col 
    
    for neg dig (0,0),(1,1),(2,2) ->  r-c = 0 
    for neg dig  (0,1),(1,2)  -> r-c = 1 
    row-col 
    
    for a row -> r dfs(r)
    checking all col where to place the q

        
    '''