class Node:
  def __init__(self,val):
    self.val = val
    self.link = None 
class List:
  def __init__(self):
    self.head = None 
  def insert_big(self,val):
    if(self.head is None):
      self.head = Node(val)
    else:
      v = Node(val)
      ctr = self.head 
      while(ctr.link is not None):
        ctr = ctr.link 
      ctr.link = v 
  def display(self):
    if self.head is None:
      print("Empty")
    ctr = self.head 
    while(ctr is not None):
      print(ctr.val,end=" ")
      ctr = ctr.link 
  def insert(self,val,pos):
    ctr = self.head 
    count = 0
    while(ctr is not None):
      count+=1 
      k = ctr  
      ctr = ctr.link
      if(count==pos):
        n = Node(val)
        print([ctr.val,k.val])
        n.link = ctr
        k.link = n 
ist = List()
lis= list(map(int,input().split()))
for i in lis:
  ist.insert_big(i)
ist.display()
ist.insert(10,4)
ist.display()