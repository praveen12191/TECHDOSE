from sortedcontainers import SortedList
class Solution:
    def combinationSum(self, cand: List[int], target: int) -> List[List[int]]:
        l = len(cand)
        res = []
        def find(tar,ind,ans,sm):
            if(sm>tar):
                return 
            if(sm==tar):
                res.append(ans[0:len(ans)])
            for i in range(ind,l):
                ans.append(cand[i])
                sm+=cand[i]
                find(tar,i,ans,sm)
                ans.pop()
                sm-=cand[i]
        find(target,0,[],0)
        return res