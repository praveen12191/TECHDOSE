# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        lis = []
        ptr = head 
        while(ptr):
            lis.append(ptr.val)
            ptr = ptr.next 
        tl = (m*n)-len(lis)
        for i in range(tl):
            lis.append(-1)
        ans = [[0 for i in range(n)] for i in range(m)]
        sm = 0 
        row = m
        col = n 
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
                    ans[k1][i] = lis[ctr]
                    ctr+=1
                k1+=1 
                k1_end-=1 
                k1_start+=1
            elif(k==2):
                for i in range(k2_start,k2_end):
                    ans[i][k2] =  lis[ctr]
                    ctr+=1
                k2_end-=1
                k2-=1
                k2_start+=1
            elif(k==3):
                for i in range(k3_start,k3_end-1,-1): 
                    ans[k3][i] = lis[ctr]
                    ctr+=1
                k3_start-=1 
                k3_end+=1 
                k3-=1
            else:
                k = 0 
                for i in range(k4_start,k4_end,-1): 
                    ans[i][k4] = lis[ctr]
                    ctr+=1
                k4+=1 
                k4_start-=1 
                k4_end+=1
            k+=1 
        return ans