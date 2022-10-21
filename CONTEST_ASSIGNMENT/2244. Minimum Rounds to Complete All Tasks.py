class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ctr = Counter(tasks)
        ans = 0 
        for i,j in ctr.items():
            if(j==1):
                return -1 
            '''
            3333 - > 4 
            4%3 = 1 
            4 = 3*x +1 
            x = (4-1)//3
            '''
            if(j%3==0):
                ans+= j//3 
            elif(j%3==1):
                x = (j-1)//3
                ans+= x+1 
            elif(j%3==2):
                x = (j-2)//3 
                ans+= x+1 
        return ans