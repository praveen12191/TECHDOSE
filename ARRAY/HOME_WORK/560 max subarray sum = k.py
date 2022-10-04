class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        has = defaultdict(int)
        sm = 0 
        has = {0:1}
        lis = [nums[0]]
        for i in nums[1::]:
            lis.append(lis[-1]+i)
        ctr = 0
        print(lis)
        for i in lis:
            if(i-k in has):
                ctr+=has[i-k]
            if(i in has):
                has[i]+=1 
            else:
                has[i] = 1
        print(has)
        return ctr