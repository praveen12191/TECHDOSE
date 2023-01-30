class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix)
        lis = []
        for i in range(l):
            k = []
            for j in range(l):
                k.append(matrix[j][i])
            lis.append(k[::-1])
        for i in range(l):
            for j in range(l):
                matrix[i][j] = lis[i][j]
        return matrix
        