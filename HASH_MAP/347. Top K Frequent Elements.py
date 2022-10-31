class Solution:
    def topKFrequent(self, nums: List[int], k1: int) -> List[int]:
        k = Counter(nums)
        ans = []
        for i,j in sorted(k.items(),key=lambda x: -x[1]):
            k1-=1
            ans.append(i)
            if(k1==0):
                return ans
            