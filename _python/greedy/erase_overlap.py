class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        latest = -float("inf")
        deletes = 0
        for interval in intervals:
            start, end = interval

            if start < latest:
                # handle overlap by finding which one has smaller end, we delete the larger one
                latest = min(latest, end)
                deletes += 1
            else:
                latest = end

        return deletes


s = Solution()
intervals = [[1, 2], [2, 4], [1, 4]]
print(s.eraseOverlapIntervals(intervals))

intervals = [[1, 2], [2, 4]]
print(s.eraseOverlapIntervals(intervals))
