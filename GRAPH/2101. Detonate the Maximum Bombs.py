class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            for j in range(n):
                if(i!=j):
                    b1,b2 = bombs[i],bombs[j]
                    if((b1[0]-b2[0])**2 + (b1[1]-b2[1])**2 <=b1[2]**2):
                        adj[i].append(j)
        '''
          [2,1,3] [6,1,4]
          dis (2-6)**2 + 0 <=9 no not cover entire distance
          but (6-2)**2 .. 16<=16 in the fig [6,1,4] covers [2,1,3]
        '''
        mx = 1
        print(adj)
        for x in range(n):
            que = [x]
            vis = set()
            count = 0 
            while(que):
                ctr = que.pop(0)
                count+=1
                vis.add(ctr)
                for i in adj[ctr]:
                    if(i not in vis):
                        que.append(i)
                        vis.add(i)
            mx = max(mx,count)
        return mx
