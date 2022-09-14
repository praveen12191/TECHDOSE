class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return 0
        val1 = x 
        ctr = 0
        while(val1>0):
            ctr = ctr*10 + val1%10 
            val1 = val1//10
            
        if(ctr==x):
            return 1 
        return 0