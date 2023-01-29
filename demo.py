class Node():
    def __init__(self,val):
        self.val = val
        self.next = None 
class link:
    def __init__(self):
        self.ctr = None
        self.ptr = None
    def append(self,val):
        v = Node(val)
        if(self.ctr==None):
            self.ptr = v
            self.ctr = self.ptr 
        else:
            k = self.ctr
            k2 = None
            while(k):
                k2 = k 
                k = k.next 
            k2.next  = v 
            self.ctr = k2.next
    def display(self):
        k = self.ptr 
        while(k):
            print(k.val)
            k = k.next 
lis = [1,2,3,4]
ptr = link()
for i in lis:
    ptr.append(i)
ptr.display()
    
            
            