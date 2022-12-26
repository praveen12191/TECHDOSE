# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ctr = 1
        ans = []
        qu = [root]
        while(qu):
            k = []
            for i in range(len(qu)):
                ptr = qu.pop(0)
                if(ptr):
                    k.append(ptr.val)
                    if(ptr.left):
                        qu.append(ptr.left)
                    if(ptr.right):
                        qu.append(ptr.right)
            if(k and ctr%2==1):
                ans.append(k)
            elif(k):
                ans.append(k[::-1])
            ctr+=1
        return ans