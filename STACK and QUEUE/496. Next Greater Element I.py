class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums2)
        stack = []
        for i in range(len(nums2)):
            while(stack and nums2[stack[-1]]<=nums2[i]):
                res[stack.pop()] = nums2[i]
            stack.append(i)
        ans = []
        for i in nums1:
            ind = nums2.index(i)
            ans.append(res[ind])
        return ans