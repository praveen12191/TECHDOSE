# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root,par):
            if(root):
                root.par = par
                dfs(root.left,root)
                dfs(root.right,root)
        dfs(root,None)
        # make as graph 
        def find(root):
            if(root):
                print(root.val,root.par)
                find(root.left)
                find(root.right)
        que = [[target,0]]
        vis = {}
        ans = []
        while(que):
            ctr,ind = que.pop(0)
            if(ctr):
                if(ind==k):
                    ans.append(ctr.val)
                vis[ctr] = 1 
                if(ctr.par not in vis):
                    que.append([ctr.par,ind+1])
                if(ctr.left not in vis):
                    que.append([ctr.left,ind+1])
                if(ctr.right not in vis):
                    que.append([ctr.right,ind+1])
        return ans
