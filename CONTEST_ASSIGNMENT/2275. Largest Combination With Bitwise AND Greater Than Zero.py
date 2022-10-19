class Solution:
    def largestCombination(self, can: List[int]) -> int:
        mx = 0
        for i in range(33):
            ctr = 0
            for x in can:
                if(x&1<<i):
                    ctr+=1
            mx = max(ctr,mx)
        return mx