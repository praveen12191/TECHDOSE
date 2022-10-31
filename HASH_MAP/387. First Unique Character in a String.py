class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = len(s)
        lis = [0 for i in range(127)]
        for i in s:
            lis[ord(i)]+=1
        ctr = 0
        for i in s:
            if(lis[ord(i)]==1):
                return ctr 
            ctr+=1
        return -1