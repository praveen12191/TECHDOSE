class Solution:
    def merge(self, nums: List[List[int]]) -> List[List[int]]:
        
        '''
        [1,3],[2,6],[4,8],[10,20]
        1st k1 = [1,3]
        2nd else: 3 = max(3,6)->[1,6]
        3rd else: 6 = max(6,8)->[1,8]
        4th [1,8],[10,20]
        '''
        nums.sort()
        val = []
        l = len(nums)
        for i in range(l):
            if(val and val[-1][1]>=nums[i][0]):
                val[-1][1] = max(nums[i][1],val[-1][1])
            else:
                val.append(nums[i])
        return val