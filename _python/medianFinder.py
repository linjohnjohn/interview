import heapq

class MedianFinder:
    def __init__(self):
        # min heap is the larger right hand half of stream
        self.minHeap = []
        heapq.heapify(self.minHeap)
        # max heap is the smaller left hand half of stream
        self.maxHeap = []
        heapq.heapify(self.maxHeap)

    def addNum(self, num: int) -> None:
        if len(self.minHeap) > len(self.maxHeap):
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)
        
        if (self.minHeap and self.maxHeap and self.minHeap[0] < -self.maxHeap[0]):
            tmp = heapq.heapreplace(self.minHeap, -self.maxHeap[0])
            heapq.heapreplace(self.maxHeap, -tmp)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        else:
            return self.minHeap[0]
        

s = MedianFinder()
s.addNum(1)
print(s.findMedian())

s.addNum(2)
print(s.findMedian())

s.addNum(3)
print(s.findMedian())

s.addNum(4)
print(s.findMedian())
