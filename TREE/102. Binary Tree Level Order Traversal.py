# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return 
        arr = []
        v = []
        arr.append(root)
        while(len(arr)):
            k = []
            for i in range(len(arr)):
                val = arr.pop(0)
                k.append(val.val)
                if(val.left is not None):
                    k1 = val.left 
                    arr.append(k1)
                if(val.right is not None):
                    k1 = val.right 
                    arr.append(k1)
            if(len(k)!=0):
                v.append(k)
        return v
            
            