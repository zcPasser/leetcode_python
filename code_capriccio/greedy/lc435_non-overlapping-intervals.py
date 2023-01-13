class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        len_intervals = len(intervals)
        if len_intervals == 0:
            return 0
        intervals.sort(key=lambda x: x[1])
        cnt = 1
        end = intervals[0][1]
        for i in range(1, len_intervals):
            if intervals[i][0] >= end:
                cnt += 1
                end = intervals[i][1]
        return len_intervals - cnt