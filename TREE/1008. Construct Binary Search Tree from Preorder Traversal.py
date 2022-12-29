# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        l = len(preorder)
        def build(start,end):
            if(self.ctr<l and start<=preorder[self.ctr]<=end):
                root = TreeNode(preorder[self.ctr])
                self.ctr+=1 
                root.left = build(start,root.val)
                root.right = build(root.val,end)
                return root
            return None
        self.ctr = 0 
        return build(-float('inf'),float('inf'))

