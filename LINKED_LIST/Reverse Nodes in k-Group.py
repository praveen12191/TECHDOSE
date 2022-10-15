# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lis = []
        ptr = head
        while(ptr):
            lis.append(ptr.val)
            ptr = ptr.next
        l = len(lis)
        ans,ctr,count = [],[],0
        for i in range(l):
            count+=1 
            ctr.append(lis[i])
            if(count==k):
                ans+=ctr[::-1]
                ctr = []
                count = 0
        ans = ans+lis[l-l%k::]
        ptr = 0 
        ptr = None
        for i in range(l):
            if(i==0):
                ptr = ListNode(ans[i])
            else:
                k = ptr 
                while(k.next):
                    k = k.next 
                k.next = ListNode(ans[i])
        return ptr