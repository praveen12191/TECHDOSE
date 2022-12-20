# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def find(root,left,right):
            if(root is None):
                return 1
            if(root.val>left and root.val<right):
                return find(root.left,left,root.val) and find(root.right,root.val,right)
            else:
                return 0 
        return find(root,-inf,inf)

        