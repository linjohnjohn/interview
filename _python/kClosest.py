
import heapq

class Solution:    
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if (len(maxHeap) > k):
                heapq.heappop(maxHeap)
        
        
        return list(map(lambda x: [x[1], x[2]], maxHeap))
    
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minHeap = []

        for n in nums:
            heapq.heappush(minHeap, n)
            if (len(minHeap) > k):
                heapq.heappop(minHeap)
        
        return heapq.heappop(minHeap)


s = Solution()
print(s.kClosest([[1, 1], [2, 2], [1, 2]], 2))
print(s.findKthLargest([2, 2, 1, 1, 2, 1, 4, 12, 3, 2], 2))
