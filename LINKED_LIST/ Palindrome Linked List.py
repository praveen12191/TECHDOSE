# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head 
        while(fast and fast.next):
            slow = slow.next 
            fast = fast.next.next 
        ptr = None
        while(slow):
            k = slow.next 
            slow.next = ptr 
            ptr = slow 
            slow = k 
        while(ptr):
            if(ptr.val != head.val):
                return 0 
            ptr = ptr.next 
            head = head.next
        return 1