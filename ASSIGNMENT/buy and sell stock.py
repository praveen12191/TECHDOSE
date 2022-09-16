class Solution:
    def maxProfit(self, p: List[int]) -> int:
        mn,mx = float('inf'),0 
        for i in p:
            mn = min(mn,i)
            mx = max(mx,i-mn)
        return mx