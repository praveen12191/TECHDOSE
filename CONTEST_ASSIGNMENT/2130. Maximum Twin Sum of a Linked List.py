# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if(head is None):
            return 
        lis = []
        ptr = head 
        while(ptr):
            lis.append(ptr.val)
            ptr = ptr.next
        l = len(lis)
        end = len(lis)-1
        start = 0
        mx = 0
        for i in range(l//2):
            mx = max(mx,lis[start]+lis[end])
            start+=1 
            end-=1
        return mx