from ast import Break


class node:
    def __init__(self,val):
        self.val = val 
        self.ptr = 0
class XOR:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,k):
        nd = node(k)
        if(self.head is None):
            self.head = nd
            self.tail = nd
        else:
            self.tail.ptr = (self.tail.ptr ^ id(nd))
            nd.ptr = id(self.tail)
            self.tail = nd 
    def display(self):
        ctr = self.head 
        k = ctr.ptr ^ 0 
        print(ctr.ptr.val)
        
    
    
lis = [1,2,3,4,5]
o = XOR()
for i in lis:
    o.append(i)
o.display()