from sortedcontainers import SortedList
class NumberContainers:

    def __init__(self):
        self.has = defaultdict(SortedList)
        self.min = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if(index in self.min):
            num = self.min[index]
            self.has[num].discard(index)
        self.min[index] = number
        self.has[number].add(index)
    def find(self, number: int) -> int:
        if(number in self.has):
            if(len(self.has[number])==0):
                return - 1
            return self.has[number][0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)