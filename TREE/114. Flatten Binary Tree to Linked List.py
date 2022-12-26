# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        lis = []
        def find(root):
            if(root):
                lis.append(root.val)
                find(root.left)
                find(root.right)
        find(root)
        print(lis)
        if(len(lis)==0):
            return []
        ptr = TreeNode(lis[0])
        ctr = ptr
        for i in lis[1:]:
            ctr.right = TreeNode(i)
            ctr = ctr.right 
        root.left = None
        root.right = ptr.right