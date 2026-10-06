class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        start, end = newInterval
        l, r = 0, len(intervals)

        # find first interval that contains start by finding first interval
        # that is greater than start, then going back one interval
        while l < r:
            m = l + (r - l) // 2
            c_s, c_e = intervals[m]

            if c_s < start:
                l = m + 1
            else:
                r = m

        idx = l

        l, r = 0, len(intervals)
        # find first interval that contains end by finding first interval
        # that has an e greater than end
        while l < r:
            m = l + (r - l) // 2
            c_s, c_e = intervals[m]

            if c_e < end:
                l = m + 1
            else:
                r = m

        if idx == 0:
            if end < intervals[idx][0]:
                intervals.insert(0, newInterval)
            else:
                intervals[idx][0] = min(intervals[idx][0], newInterval[0])
                intervals[idx][0] = min(intervals[idx][1], newInterval[1])
