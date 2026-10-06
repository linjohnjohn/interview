# Problem: Non-overlapping Intervals
# Remove the fewest intervals so the remaining intervals do not overlap. Intervals touching at
# endpoints are allowed.
#
# Expected input/output: intervals=[[1,2],[2,3],[3,4],[1,3]] -> 1; intervals=[[1,2],[2,3]] ->
# 0

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


# Key insight:
# When intervals overlap, retain the one ending earlier; it leaves at least as much room for
# every future interval.
