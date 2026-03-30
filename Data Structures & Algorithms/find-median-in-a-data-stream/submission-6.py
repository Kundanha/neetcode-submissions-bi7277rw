class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        largest_left = -heapq.heappop(self.maxHeap)

        heapq.heappush(self.minHeap, largest_left)

        if len(self.minHeap) > len(self.maxHeap):
            smallest_right = -heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, smallest_right)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0])/2.0
        
        