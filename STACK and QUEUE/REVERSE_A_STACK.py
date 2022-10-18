class Node:
    def __init__(self,val):
        self.next = None 
        self.val = val 
class List:
    def __init__(self):
        self.top = None 
    
    def add(self,val):
        k = Node(val)
        if(not self.top):
            self.top = k 
            return 
        k.next = self.top 
        self.top = k 
    def display(self):
        ptr = self.top 
        while(ptr):
            print(ptr.val,end=" ")
            ptr = ptr.next
    def reverse(self):
        ctr = None 
        ctr2 = self.top
        while(ctr2):
            ptr = ctr2
            ctr2 = ctr2.next 
            ptr.next = ctr 
            ctr = ptr 
        self.top = ctr
        ptr = ctr
        
        
obj = List()
lis = [1,2,3,4,5]
for i in lis:
    obj.add(i)
obj.display()
obj.reverse()
print()
obj.display()