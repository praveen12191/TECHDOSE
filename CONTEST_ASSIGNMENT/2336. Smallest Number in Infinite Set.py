class SmallestInfiniteSet:

    def __init__(self):
        self.lis = [i for i in range(10001)]
        self.pop = []
        self.ind = 1
    def popSmallest(self) -> int:
        self.lis.sort()
        return self.lis.pop(self.ind)
    def addBack(self, num: int) -> None:
        if(num in self.lis):
            pass
        else:
            self.lis.append(num)
            self.ind = 1


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)