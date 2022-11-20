

class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        v1 = (points[0][0] - points[1][0], points[0][1] - points[1][1])
        v2 = (points[1][0] - points[2][0], points[1][1] - points[2][1])

        return v1[0] * v2[1] != v1[1] * v2[0]
        # exclude the case where the slope does not exist
        # def get_slope(point1: [int, int], point2: [int, int]):
        #     return 1.0 * (point1[1] - point2[1]) / (point1[0] - point2[0])
        # if points[0][0] == points[1][0]:
        #     if points[1][0] == points[2][0] or points[0][1] == points[1][1]:
        #         return False
        #     else:
        #         return True
        # elif points[1][0] == points[2][0]:
        #     if points[2][0] == points[0][0] or points[1][1] == points[2][1]:
        #         return False
        #     else:
        #         return True
        # else:
        #     return get_slope(points[0], points[1]) != get_slope(points[1], points[2])



points = [[0,0],[1,1],[1,1]]
s = Solution()
print(s.isBoomerang(points))