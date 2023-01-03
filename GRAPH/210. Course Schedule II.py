class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for i,j in pre:
            adj[i].append(j)
        ans = []
        col = [0]*n
        def kahn_algo():
            indegree = [0]*n
            for i,j in pre:
                indegree[j]+=1 
            que = [i for i in range(n) if indegree[i]==0]
            ans = []
            while(que):
                ctr = que.pop(0)
                ans.append(ctr)
                for i in adj[ctr]:
                    indegree[i]-=1 
                    if(indegree[i]==0):# inde will be 0 
                        que.append(i)
            if(len(ans)!=n):
                #there is a cycle
                return []
            else:
                return ans[::-1]
        def dfs(ctr):
            if(col[ctr]==-1): #cycle 
                return 1
            if(col[ctr]==1):
                return 0 
            col[ctr] = -1 
            for i in adj[ctr]:
                if(dfs(i)==1):
                    return 1 
            col[ctr] = 1
            ans.append(ctr)
            return 0
        for i in range(n):
            if(dfs(i)==1):
                return [] 
        return ans
        # return kahn_algo()