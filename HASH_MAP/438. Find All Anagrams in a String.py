class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        has1 = Counter(p)
        has2 = Counter(s[0:len(p)])
        l1 = len(s)
        l2 = len(p)
        ans = []
        for i in range(l1-l2):
            if(has1==has2):
                ans.append(i)
            has2[s[i]]-=1
            if(has2[s[i]]==0):
                del has2[s[i]]
            has2[s[i+l2]]+=1 
        if(has1==has2):
            ans.append(l1-l2)
        return ans