class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        val = 0 
        lis = []
        l = len(encoded)
        for i in range(1,l+2):
            val^=i 
        val2 = 0 
        for i in range(1,l,2):
            val2^=encoded[i]
        lis.append(val^val2)