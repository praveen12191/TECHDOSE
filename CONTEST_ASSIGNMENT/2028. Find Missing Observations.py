class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        l = len(rolls)+n
        sm = sum(rolls)
        ans = (l*mean)-sm
        if(ans<n or ans>n*6):
            return []
        part = ans//n
        rem = ans%n
        lis = []
        for i in range(n):
            lis.append(part)
        for i in range(rem):
            lis[i]+=1 
        return lis