# Problem: Find Median from Data Stream
# Support adding integers and querying the median of all values seen. Average the middle two
# values for an even count; queries have at least one value.
#
# Expected input/output: addNum(1), addNum(2), findMedian() -> 1.5; addNum(3), findMedian() ->
# 2

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


# Key insight:
# Keep a max-heap of the lower half and a min-heap of the upper half, balanced in size with
# every lower value no greater than every upper value.
