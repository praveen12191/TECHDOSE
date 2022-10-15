# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lis = []
        ptr = head 
        if(head is None):
            return head
        while(ptr.next is not None):
            lis.append(ptr.val)
            ptr = ptr.next 
        k = ptr
        k2 = ptr
        lis.append(ptr.val)
        lis.sort()
        for i in lis:
            k1 = ListNode(i)
            k.next = k1 
            k = k1 
        return k2.next