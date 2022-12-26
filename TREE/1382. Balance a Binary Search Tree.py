# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        lis = []
        def find(root):
            if(root):
                lis.append(root.val)
                find(root.left)
                find(root.right)
        find(root)
        lis.sort()
        def build(start,end):
            if(start>end):
                return None
            mid = start+(end-start)//2
            ctr = TreeNode(lis[mid])
            ctr.left = build(start,mid - 1)
            ctr.right = build(mid+1,end)
            return ctr 
        return build(0,len(lis)-1)


