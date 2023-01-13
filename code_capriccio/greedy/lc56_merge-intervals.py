class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        len_intervals = len(intervals)
        ans = []
        if len_intervals == 0:
            return ans
        intervals.sort(key=lambda x: x[0])
        ans.append(intervals[0])
        for i in range(1, len_intervals):
            if ans[-1][1] >= intervals[i][0]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1])
            else:
                ans.append(intervals[i])
        return ans
