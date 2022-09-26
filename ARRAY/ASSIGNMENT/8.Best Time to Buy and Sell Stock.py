class Solution:
    def maxProfit(self, p: List[int]) -> int:
        mx = 0 
        mn = float('inf')
        for i in p:
            if(i<mn):
                mn = i 
            else:
                mx = max(mx,i-mn)
        return mx