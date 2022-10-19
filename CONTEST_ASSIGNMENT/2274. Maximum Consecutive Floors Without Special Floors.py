class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        m1 = min(special)-bottom
        m2 = top - max(special)
        l = len(special)
        special.sort()
        m3 = 0
        for i in range(l-1):
            m3 = max(m3,special[i+1]-special[i])
        if(m3!=0):
            m3-=1
        mx = max(m1,m2)
        mx = max(mx,m3)
        return mx