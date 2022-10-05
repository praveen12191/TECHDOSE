class MedianFinder:

    def __init__(self):
        self.lis = []

    def addNum(self, num: int) -> None:
        self.lis.append(num)

    def findMedian(self) -> float:
        l = len(self.lis)
        self.lis.sort()
        if(l%2==0):
            return (self.lis[l//2] + self.lis[l//2-1])/2
        else:
            k = self.lis[l//2]
            return k


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()