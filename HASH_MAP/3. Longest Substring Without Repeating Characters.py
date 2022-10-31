class Solution:
    def __init__(self):
        self.mx = 0
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(has):
            for i,j in has.items():
                if(j!=1):
                    return 1
            self.mx = max(self.mx,len(has))
            return 0
            
        start,l = 0,len(s)
        ctr,end = 0,0
        has = defaultdict(int)
        while(start<l):
            has[s[start]]+=1 
            if(check(has)):
                for i in range(end,start+1):
                    has[s[i]]-=1 
                    if(has[s[i]]==0):
                        del has[s[i]]
                    if(check(has)==0):
                        end = i+1
                        break 
            start+=1
        return self.mx
        
            