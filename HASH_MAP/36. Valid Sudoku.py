class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)
        for i in range(l):
            for j in range(l):
                if(board[i][j]!='.'):
                    if(self.find(board,i,j,board[i][j])==0):
                        return 0 
        return self.find2(board)
        for i in board:
            print(i)
        return 1
        
    def find(self,board,x,y,val):
        l = len(board)
        
        for i in range(l):
            if(i!=x and board[i][y]==val):
                return 0
        for i in range(l):
            if(i!=y and board[x][i]==val):
                return 0 
        return 1
    def find2(self,board):
        l = len(board)
        for i in range(0,l,3):
            for j in range(0,l,3):
                lis = []
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        k = board[x][y]
                        print(k,end=" ")
                        if(k.isdigit()):
                            if(k in lis):
                                return 0 
                            lis.append(k)
        return 1 