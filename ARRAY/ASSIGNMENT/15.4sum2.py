class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        has = defaultdict(int)
        for i in nums3:
            for j in nums4:
                has[i+j]+=1 
        ctr = 0
        print(has)
        for i in nums1:
            for j in nums2:
                if(-1*(i+j) in has):
                    ctr+=has[-1*(i+j)]
        return ctr