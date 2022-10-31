class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lis = []
        has ={}
        for i in strs:
            k = sorted(i)
            k = str(k)
            if(k in has):
                has[k].append(i)
            else:
                has[k] = [i]
        ans = []
        for i,j in has.items():
            ans.append(j)
        return ans