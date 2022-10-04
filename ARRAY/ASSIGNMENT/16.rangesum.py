class NumArray:

    def __init__(self, nums: List[int]):
        self.lis = nums
        self.pref = [nums[0]]
        for i in nums[1::]:
            self.pref.append(self.pref[-1]+i)

    def sumRange(self, left: int, right: int) -> int:
        if(left==0):
            return self.pref[right]
        val1 = self.pref[left-1]
        val2 = self.pref[right]
        return val2-val1



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)