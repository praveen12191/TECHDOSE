class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l = len(number)
        mx = 0 
        for i in range(l):
            if(number[i]==digit):
                k = number[0:i]+number[i+1::]
                mx = max(int(k),mx)
        return str(mx)