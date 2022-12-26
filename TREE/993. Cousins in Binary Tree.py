# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.d1,self.d2 = 0,0
        self.p1,self.p2 = 0,0
        self.dep = 0 
        def find(dep,root,par):
            if(root):
                self.dep = max(self.dep,dep)
                if(root.val==x):
                    self.d1 = dep
                    self.p1 = par
                if(root.val==y):
                    self.d2 = dep
                    self.p2 = par
                find(dep+1,root.left,root)
                find(dep+1,root.right,root)
        find(0,root,root)
        print(self.d1,self.d2,self.dep)
        if(self.d1==self.d2 and self.dep-self.d1==self.dep-self.d2 and self.p1!=self.p2):
            return 1
        return 0



