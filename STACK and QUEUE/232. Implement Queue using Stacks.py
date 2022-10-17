class MyQueue:

    def __init__(self):
        self.top = - 1
        self.lis = []
        
    def push(self, x: int) -> None:
        self.lis.append(x)
        self.top+=1

    def pop(self) -> int:
        k1,k2 = self.top,self.lis[0]
        newlis = []
        while(k1!=0):
            newlis.append(self.lis[k1])
            k1-=1 
        self.top-=1 
        self.lis = newlis[::-1]    
        return k2
    def peek(self) -> int:
        return self.lis[0]

    def empty(self) -> bool:
        if(self.top==-1):
            return 1
        return 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()