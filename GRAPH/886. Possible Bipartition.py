class Solution:
    def possibleBipartition(self, n: int, dis: List[List[int]]) -> bool:
        col = [-1 for i in range(n+1)]
        adj = defaultdict(list)
        for i,j in dis:
            adj[i].append(j)
            adj[j].append(i)
        for i in range(n):
            if(col[i]==-1):
                if(self.bfs(i,adj,col)==0):
                    return 0 
        return 1
    def bfs(self,val,adj,col):
        que = [val]
        col[val] = 1
        while(que):
            ptr = que.pop(0)
            ctr_col = col[ptr]
            for j in adj[ptr]:
                if(col[j]==-1):
                    col[j] = 1-ctr_col
                    que.append(j)
                if(col[j]==ctr_col):
                    return 0 
        return 1


