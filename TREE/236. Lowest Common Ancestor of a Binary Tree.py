# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root):
            if(root):
                if(root==p or root==q):
                    return root
                left = find(root.left)
                right = find(root.right)
                if(left==None):
                    return right
                elif(right==None):
                    return left 
                else:
                    return root
        return find(root)
        '''
        for (5,8) 
        5 == p so return 5 
        8 == q return 8 and 1 will return 8 
        so both side not null so root 
        if( left is null return right)
        '''