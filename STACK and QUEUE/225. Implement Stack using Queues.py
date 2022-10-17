class MyStack:

    def __init__(self):
        self.lis = []
        self.front = -1 
        self.rear = - 1
    def push(self, x: int) -> None:
        self.lis.append(x)
        if(self.front==-1 and self.rear==-1):
            self.front+=1 
            self.rear+=1 
        else:
            self.rear+=1 

    def pop(self) -> int:
        newlis = []
        k = self.lis[self.rear]
        for i in range(self.front,self.rear):
            newlis.append(self.lis[i])
        self.rear-=1 
        self.lis = newlis 
        return k

    def top(self) -> int:
        return self.lis[self.rear]
    def empty(self) -> bool:
        if(self.rear==-1):
            return 1 
        return 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()