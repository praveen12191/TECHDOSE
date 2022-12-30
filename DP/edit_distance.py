class Solution(object):
    def minDistance(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        lis = []
        for i in range(l1+1):
            lis.append([0 for i in range(l2+1)])
        for i in range(l1+1):
            for j in range(l2+1):
                if(i==0):
                    lis[i][j] = j 
                elif(j==0):
                    lis[i][j] = i 
                elif(word1[i-1]==word2[j-1]):
                    lis[i][j] = lis[i-1][j-1]
                else:
                    lis[i][j] = 1+min(lis[i-1][j],lis[i-1][j-1],lis[i][j-1])
        return lis[l1][l2]
        