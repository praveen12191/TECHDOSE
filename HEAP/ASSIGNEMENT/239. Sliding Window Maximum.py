class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = len(nums)
        ans,de = [],collections.deque()
        for i in range(l):
            while(de and de[0]<=i-k):# if we going beond the limets
                de.popleft()
            while(de and nums[de[-1]]<nums[i]):
                de.pop()
            de.append(i)
            if(i-k+1>=0):
                ans.append(nums[de[0]])
        return ans
    '''
        [1,3,-1,-3,5,3,6,7]
        ------- de 3 so we appending our ans 
            ------ de 3 -1 -3 append
               ----- here we no need 3 in de because it is not in range so need to remove...
    '''