class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l = len(matrix)
        lis = []
        for i in range(l):
            lis+=matrix[i] 
        lis.sort()
        return lis[k-1]
