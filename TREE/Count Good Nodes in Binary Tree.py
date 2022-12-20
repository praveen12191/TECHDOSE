# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.mx = root.val
        self.ctr = 0
        def find(node,mx):
            if(node):
                if(mx<=node.val):
                    mx = node.val
                    self.ctr+=1 
                find(node.left,mx)
                find(node.right,mx)
        find(root,-float('inf'))
        return self.ctr