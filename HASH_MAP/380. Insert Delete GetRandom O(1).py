class RandomizedSet:

    def __init__(self):
        self.has = defaultdict(int)
        self.val = []

    def insert(self, val: int) -> bool:
        if(val not in self.has):
            self.val.append(val) 
            self.has[val]+=1
            return 1
        return 0

    def remove(self, val: int) -> bool:
        if(val in self.val):
            ind = self.val.index(val)
            del self.val[ind]
        if(val in self.has):
            del self.has[val]
            return 1
        return 0 

    def getRandom(self) -> int:
        return choice(self.val)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()