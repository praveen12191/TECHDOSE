from collections import *

class Solution:
    def longestUniqueSubsttr(self, s):
        l = len(s)
        start,end,mx = 0,0,0 
        has = defaultdict(int)
        f = 0 
        while(start<l):
            has[s[start]]+=1 
            if(has[s[start]]!=1):
                f = 1
                mx = max(mx,len(has))
                for i in range(end,l):
                    if(s[i]!=s[start]):
                        if(s[i] in has):
                            del has[s[i]]
                    else:
                        end = i+1
                        has[s[start]]-=1
                        break 
            start+=1
        mx = max(mx,len(has))
        return mx


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        s = input().strip()
        
        
        ob=Solution()
        print(ob.longestUniqueSubsttr(s))
# } Driver Code Ends