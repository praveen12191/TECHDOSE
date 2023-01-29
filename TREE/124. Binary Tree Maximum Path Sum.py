# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mx = -float('inf')
        def find(root):
            if(root==None):
                return 0 
            left = find(root.left)
            right = find(root.right)
            if(left<0):
                left = 0 
            if(right<0):
                right = 0
            self.mx = max(self.mx,left+right+root.val)
            return max(left,right)+root.val
        find(root)
        return self.mx