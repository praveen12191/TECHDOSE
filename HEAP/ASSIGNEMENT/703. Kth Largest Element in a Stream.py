class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k 
        while(self.k<len(self.nums)):
            heapq.heappop(self.nums)
    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        while(self.k<len(self.nums)):
             heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)æ
# param_1 = obj.add(val)