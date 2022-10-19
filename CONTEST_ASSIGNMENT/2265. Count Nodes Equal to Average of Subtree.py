# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sm = 0
        self.n = 0
        self.ctr = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if(root):
                val = root.val
                ans = find(root)
                if(self.sm//self.n==val):
                    self.ctr+=1
                self.sm = 0 
                self.n = 0
                dfs(root.left)
                dfs(root.right)
        def find(root):
            if(root):
                self.sm+=root.val
                self.n+=1
                find(root.left)
                find(root.right)
        dfs(root)
        return self.ctr
            