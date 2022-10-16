# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        ptr = head 
        sm = 0 
        ptr = ptr.next
        ctr = None
        while(ptr):
            if(ptr.val==0):
                if(ctr is None):
                    ctr = ListNode(sm)
                    k = ctr
                else:
                    k.next = ListNode(sm)
                    k = k.next
                sm = 0 
            else:
                sm+=ptr.val 
            ptr = ptr.next 
        return ctr