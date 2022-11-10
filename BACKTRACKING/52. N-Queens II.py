class Solution:
    def __init__(self):
        self.count = 0
    def totalNQueens(self, n: int) -> int:
        pos_dig = set()
        neg_dig = set()
        ctr = set()
        def backtrack(r):
            if(r==n):
                self.count+=1
            for c in range(n):
                if(r+c in pos_dig or r-c in neg_dig or c in ctr):
                    continue 
                pos_dig.add(r+c)
                neg_dig.add(r-c)
                ctr.add(c)
                backtrack(r+1)
                pos_dig.remove(r+c)
                neg_dig.remove(r-c)
                ctr.remove(c)
        backtrack(0)
        return self.count