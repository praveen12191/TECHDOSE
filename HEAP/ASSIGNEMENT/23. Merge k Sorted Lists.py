# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import heapq
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lis = []
        for i in range(len(lists)):
            if(lists[i]):
                lis.append((lists[i].val,i))
        heapq.heapify(lis)
        head,ctr = None,None
        while(lis):
            data,ptr = heapq.heappop(lis)
            if(head is None):
                head = ListNode(data)
                ctr = head 
            else:
                ctr.next = ListNode(data)
                ctr = ctr.next 
            if(lists[ptr].next):
                lists[ptr] = lists[ptr].next 
                new_val = lists[ptr].val 
                heapq.heappush(lis,(new_val,ptr))
        return head
                