class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        val = Counter(s)
        ans = 0 
        while(1):
            f = 1
            for i in target:
                if(i in val):
                    val[i]-=1 
                    if(val[i]==0):
                        del val[i]
                else:
                    return ans 
            ans+=1