class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r = len(board)
        c = len(board[0])
        def dfs(i,j,ind,has):
            if(ind==len(word)):
                return 1
            if(i==-1 or i==r or j==-1 or j==c or (i,j) in has or board[i][j]!=word[ind]):
                return 0
