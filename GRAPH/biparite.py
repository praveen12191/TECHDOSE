class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj = defaultdict()
        for i in range(len(graph)):
            adj[i] = graph[i]
        l = len(graph)
        col = [-1 for i in range(l+1)]
        for i in range(l):
            if(col[i]==-1):
                if(self.bfs(col,adj,i)==0):
                    return 0 
        return 1
    def bfs(self,col,adj,val):
            st = [val]
            col[val] = 1
            while(st):
                ptr = st.pop(0)
                ctr_col = col[ptr]
                for j in adj[ptr]:
                    if(col[j]==-1):
                        col[j] = 1-ctr_col
                        st.append(j)
                    if(col[j]==ctr_col):
                        return 0 
            return 1