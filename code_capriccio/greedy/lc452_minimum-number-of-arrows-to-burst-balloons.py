class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        # points 不为空至少需要一支箭
        ans = 1
        for i in range(1, len(points)):
            # 当前气球 与 前一个气球 不重叠
            if points[i - 1][1] < points[i][0]:
                ans += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])
        return ans