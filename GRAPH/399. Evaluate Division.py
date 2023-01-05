class Solution:
    def calcEquation(self, eq: List[List[str]], v: List[float], qu: List[List[str]]) -> List[float]:
        has = defaultdict(list)
        for i in range(len(eq)):
            x,y = eq[i]
            has[x].append([y,v[i]])
            has[y].append([x,1/v[i]])
        ans = []
        for x,y in qu:
            que = [[x,y,1.0]]
            vis = set()
            f = 0 
            while(que):
                start,end,mul = que.pop(0)
                vis.add(start)
                if(start not in has or end not in has):
                    f = 1
                    ans.append(-1)
                    break
                if(start==end):
                    f = 1
                    ans.append(mul)
                    break
                for x,y in has[start]:
                    if(x not in vis):
                        que.append([x,end,mul*y])
            if(f==0):
                ans.append(-1.0)
        return ans