class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        mx = 0 
        val = 0 
        for i in nums:
            dic[i]+=1 
            k = dic[i]
            if(k>mx):
                mx = k 
                val = i 
        return val
        