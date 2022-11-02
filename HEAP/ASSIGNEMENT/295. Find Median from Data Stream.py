class MedianFinder:
    '''
        min_heap impl max_heap in py there is no max_heap so - 
        max_heap impl min_heap 
        val in min_heap < val in max_heap 
              [1,2]             [4,5]
              so finding median is easy min_heap[0]+max_heap[0]/2 
        if [1,2]    [4,5,6]
            return max_heap[0] -> imp min_heap so gives (min val)
        if [1,2]   [4]
            return min_heap[0] -> imp max_heap so give (max val)
    '''
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap,-num)
        if(self.max_heap and self.min_heap):
            if(-self.min_heap[0]>self.max_heap[0]):
                val1 = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap,-val1)
        if(len(self.max_heap) >len(self.min_heap)+1):
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap,-val)
        if(len(self.min_heap)>len(self.max_heap)+1):
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-val)
        

    def findMedian(self) -> float:
        if(len(self.min_heap)==len(self.max_heap)):
            return (-self.min_heap[0]+self.max_heap[0])/2
        elif(len(self.min_heap)>len(self.max_heap)):
            return -self.min_heap[0]
        else:
            return self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()