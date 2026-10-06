# Problem: K Closest Points to Origin; Kth Largest Element in an Array
# kClosest: Return k points nearest (0,0) by Euclidean distance; output order does not matter.
# findKthLargest: Return the kth largest array element, counting duplicates.
#
# Expected input/output: points=[[1,3],[-2,2]], k=1 -> [[-2,2]]; nums=[3,2,1,5,6,4], k=2 -> 5


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


# Key insight:
# Closest points: keep a max-heap of the k smallest squared distances. Kth largest: keep a
# min-heap of the k largest values; its root is the answer.
