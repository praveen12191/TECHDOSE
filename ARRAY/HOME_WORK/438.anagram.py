class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        v1 = Counter(p)
        lis = []
        k = s[0:len(p)]
        v2 = Counter(k)
        if(v2==v1):
            lis.append(0)
        for j in range(len(s)-len(p)):
            v2[s[j]]-=1 
            v2[s[j+len(p)]]+=1
            if(v2[s[j]]==0):
                del v2[s[j]]
            if(v2[s[j+len(p)]]==0):
                del v2[s[j+len(p)]]
            if(v1==v2):
                lis.append(j+1)
        return lis