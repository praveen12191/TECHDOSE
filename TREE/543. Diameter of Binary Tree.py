# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mx = 0 
        # depth of the node is max from left and right
        def find(root):
            if(root):
                val1 = find(root.left)
                val2 = find(root.right)
                self.mx = max(self.mx,val1+val2)
                return max(val1,val2)+1
            else:
                return 0 
        find(root)
        return self.mx
