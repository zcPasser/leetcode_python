

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        delta_x, delta_y = coordinates[0][0], coordinates[0][1]
        for point in coordinates:
            point[0] -= delta_x
            point[1] -= delta_y
        A, B = coordinates[1][1], -coordinates[1][0]
        for i in range(2, len(coordinates)):
            if A * coordinates[i][0] + B * coordinates[i][1] != 0:
                return False
        return True
        # def is_straigtht(p1: list[int], p2: list[int], p3: list[int]):
        #     v1 = (p1[0] - p2[0], p1[1] - p2[1])
        #     v2 = (p1[0] - p3[0], p1[1] - p3[1])
        #     return v1[0] * v2[1] == v1[1] * v2[0]
        #
        # for i in range(2, len(coordinates)):
        #     if not is_straigtht(coordinates[i], coordinates[i - 1], coordinates[i - 2]):
        #         return False
        #
        # return True

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
s = Solution()
print(s.checkStraightLine(coordinates))