# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ""
        ctr1 = l1
        while(ctr1 is not None):
            s1+=str(ctr1.val)
            ctr1 = ctr1.next 
        ctr2 = l2 
        s2 =""
        while(ctr2 is not None):
            s2+=str(ctr2.val)
            ctr2 = ctr2.next 
        val1 = str(int(s1[::-1])+int(s2[::-1]))
        val1 = val1[::-1]
        ctr = l1
        while(ctr.next is not None):
            ctr = ctr.next 
        ptr = ctr
        for i in val1:
            k = ListNode(int(i))
            ctr.next = k 
            ctr = k
        ptr = ptr.next
        return ptr