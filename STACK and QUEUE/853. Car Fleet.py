class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        eg (3,3),(5,2),(7,1)
        
        dis 1 to target = 3 
        dis 2           = 2.5 
        dis3            = 2.3
        2.3  2.5  3 
        last car dis is 3 with 1kmph if the next car to last car's collide with them it will converted to 1kmph 
        so we can del those car fromn stack and keep checking if some one get collide with last del it 
        in this case 2.5 is < then 3 so dis2 will go to target fast then dis1 so we del that and dis3 also the same case
        
        '''
        lis = [[x,y] for x,y in zip(position,speed)]
        stack = []
        for x,y in sorted(lis)[::-1]:
            dis = (target-x)/y
            stack.append(dis)
            if(len(stack)>=2 and stack[-1]<=stack[-2]):
                stack.pop()
        return len(stack)