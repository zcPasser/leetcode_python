"""
description:
    1、Given an array of points on the X-Y plane points where points[i] = [xi, yi]。

return:
    1、 the area of the largest triangle that can be formed by any three different points.

"""
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        def get_area_of_triangle(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
            return abs(x1 * y2 - x1 * y3 - x2 * y1 + x3 * y1 + x2 * y3 - x3 * y2) / 2

        return max([get_area_of_triangle(x1, y1, x2, y2, x3, y3) for (x1, y1), (x2, y2), (x3, y3) in combinations(points, 3)])


ps = [[1,0],[0,0],[0,1]]

s = Solution()

print(s.largestTriangleArea(ps))