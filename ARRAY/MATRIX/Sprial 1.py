class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sm = 0 
        lis = []
        row = len(matrix)
        col = len(matrix[0])
        print(row,col)
        l = row*col 
        k1 = 0
        k2 = col-1
        k1_end = col
        k2_start = 1 
        k2_end = row
        k3_start = col-2
        k3_end = 0 
        k3 = row-1
        k4_start = row-2
        k4_end = 0 
        k4 = 0 
        k = 1
        ctr = 0
        k1_start = 0 
        while(ctr!=l):
            if(k==1):
                for i in range(k1_start,k1_end):
                    ctr+=1
                    lis.append(matrix[k1][i])
                k1+=1 
                k1_end-=1 
                k1_start+=1
            elif(k==2):
                for i in range(k2_start,k2_end):
                    ctr+=1
                    lis.append(matrix[i][k2])
                k2_end-=1
                k2-=1
                k2_start+=1
            elif(k==3):
                for i in range(k3_start,k3_end-1,-1):
                    ctr+=1 
                    lis.append(matrix[k3][i])
                k3_start-=1 
                k3_end+=1 
                k3-=1
            else:
                k = 0 
                for i in range(k4_start,k4_end,-1):
                    ctr+=1 
                    lis.append(matrix[i][k4])
                k4+=1 
                k4_start-=1 
                k4_end+=1
            k+=1 
        return lis