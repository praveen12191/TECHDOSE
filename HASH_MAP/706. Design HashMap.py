class List:
    def __init__(self,key,value):
        self.key = key 
        self.value = value 
        self.next = None
class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hash = [None]*1000
    def put(self, key: int, value: int) -> None:
        ind = (key%self.size)
        ptr = self.hash[ind]
        if(ptr==None):
            self.hash[ind] = List(key,value)
            return 
        while(1):
            if(ptr.key==key):
                ptr.value = value 
                return 
            if(ptr.next==None):
                break
            ptr = ptr.next 
        # if there is no key then we can append at the end 
        ptr.next = List(key,value)
    def get(self, key: int) -> int:
        ind = (key%1000)
        ptr = self.hash[ind]
        while(ptr):
            if(ptr.key==key):
                return ptr.value 
            ptr = ptr.next 
        return -1

    def remove(self, key: int) -> None:
        ind = (key%1000)
        ptr = self.hash[ind]
        ctr = ptr 
        if(ptr==None):
            return 
        if(ptr.key==key):
            self.hash[ind] = self.hash[ind].next
            return 
        while(ptr):
            if(ptr.key==key):
                ctr.next = ptr.next
                return 
            ctr = ptr 
            ptr = ptr.next 
            
            

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)