class LRUCache:

    def __init__(self, capacity: int):
        self.has = collections.OrderedDict()
        self.tol = capacity

    def get(self, key: int) -> int:
        if(key in self.has):
            k = self.has[key]
            del self.has[key]
            self.has[key] = k 
            return k
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if(key in self.has):
            k = self.has[key]
            del self.has[key]
            self.has[key] = value
        else:
            if(len(self.has)==self.tol):
                for i,j in self.has.items():
                    del self.has[i]
                    break 
                self.has[key] = value 
            else:
                self.has[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)