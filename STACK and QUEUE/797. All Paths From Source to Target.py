class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        des = len(graph)-1
        adj = dict()
        for i in range(len(graph)):
            adj[i] = graph[i]
        ans,lis = [],[]
        def dfs(val):
            if(val==des):
                k = lis[0:len(lis)]
                k.insert(0,0)
                ans.append(k)
            for i in adj[val]:
                lis.append(i)
                find(i)
            if(lis):
                lis.pop()
        def bfs(val):
            que = [[[0],[0]]]
            while(que):
                ctr,path = que.pop(0)
                if(path[0]==des):
                    k = path[0:len(path)]
                    k=k[::-1]
                    ans.append(k)
                for i in adj[ctr[0]]:
                    que.append([[i],[i]+path])

        bfs(0)
        return ans
