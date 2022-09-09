class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ctr=0
        while(left<right):
            left=left>>1 
            right=right>>1 
            ctr+=1
        return right<<ctr