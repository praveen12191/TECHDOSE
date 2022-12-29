# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return 1
        def find(left,right):
            if(left is None and right is None):
                return 1 
            if(left is None or right is None):
                return 0 
            if(left.val==right.val):
                k1 = find(left.left,right.right)
                k2 = find(left.right,right.left)
                return k1 and k2
            else:
                return 0
        return find(root.left,root.right)