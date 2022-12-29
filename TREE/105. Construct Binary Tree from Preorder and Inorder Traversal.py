# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        l = len(preorder)
        def build(in_o,pre_o):
            if(pre_o):
                ctr = in_o.index(pre_o.pop(0))
                val = TreeNode(in_o[ctr])
                val.left = build(in_o[0:ctr],pre_o[0:ctr])
                val.right = build(in_o[ctr+1:],pre_o[ctr:])
                return val 
        return build(inorder,preorder)


