"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        vis = {}
        def dfs(node):
            if(node in vis):
                return vis[node]
            copy = Node(node.val)
            vis[node] = copy 
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))
            return copy 
        if(node):
            return dfs(node)
    '''
                        1 - []
            2-[]                        4-[]
       1-[]      3-[]
       here 1 is visited so 2-[1,]
           3-[]
    2-[]         4-[]
    here 2 is visited so 3-[2,]

            4-[]
    3-[]            1-[]

    3 and 1 are visited
    so 4-[3,1]
    so return to 3 
    3 - [2[1,],4-[3,1]]....

    '''


        