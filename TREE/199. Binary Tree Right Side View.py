# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        def find(root,dep):
            if(root):
                if(dep==len(lis)):
                    lis.append(root.val)
                find(root.right,dep+1)
                find(root.left,dep+1)
        find(root,0)
        return lis