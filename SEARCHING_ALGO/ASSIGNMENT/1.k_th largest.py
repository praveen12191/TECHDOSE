class Solution:
    def __init__(self):
        self.k1 = []
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def quick(nums,start,end,k):
            if(start<end):
                p = end-1 
                i = start-1
                for j in range(start,end):
                    if(p==j):
                        nums[i+1],nums[p] = nums[p],nums[i+1]
                        i+=1 
                    elif(nums[p]>=nums[j]):
                        nums[i+1],nums[j] = nums[j],nums[i+1]
                        i+=1 
                if(i==k):
                    val = nums[k]
                    self.k1.append(val)
                    return 0 
                elif(k<i):
                    quick(nums,start,i,k)
                else:
                    quick(nums,i,end,k)
        quick(nums,0,len(nums),len(nums)-k)
        return self.k1[0]