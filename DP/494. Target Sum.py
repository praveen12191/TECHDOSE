class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = defaultdict(int)
        def find(l,val):
            if(l==0):#need to cover all index
                if(val==target):
                    return 1
                else:
                    return 0
            if((l,val) in dp):
                return dp[(l,val)]
            res = find(l-1,val+nums[l-1])+find(l-1,val-nums[l-1])
            dp[(l,val)] = res 
            return res
        return find(l,0)