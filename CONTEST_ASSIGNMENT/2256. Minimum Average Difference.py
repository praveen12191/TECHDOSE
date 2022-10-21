class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        pref1 = [[nums[0],1]]
        ans = []
        for i in nums[1::]:
            pref1.append([pref1[-1][0]+i,pref1[-1][1]+1])
        print(pref1)
        nums = nums[::-1]
        pref2 = [[nums[0],1]]
        for i in nums[1::]:
            k1 = pref2[-1][0]
            k2 = pref2[-1][1]
            pref2.append([k1+i,k2+1])
        del pref2[-1]
        pref2 = pref2[::-1]
        pref2.append([0,1])
        for i in range(len(nums)):
            k1 = pref1[i][0]//pref1[i][1]
            k2 = pref2[i][0]//pref2[i][1]
            ans.append(abs(k1-k2))
        mn = min(ans)
        return ans.index(mn)
            
        