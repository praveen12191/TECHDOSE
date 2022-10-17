class MinStack:

    def __init__(self):
        self.lis = []
        self.t = -1
    def push(self, val: int) -> None:
        mn = self.getMin()
        mn = min(mn,val)
        self.lis.append([val,mn])
        self.t+=1
    def pop(self) -> None:
        self.lis.pop()
        self.t-=1
        
    def top(self) -> int:
        return self.lis[self.t][0]
        
    def getMin(self) -> int:
        if(self.t==-1):
            return float('inf')
        else:
            return self.lis[self.t][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()