


class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        n = len(grid)
        ans = n * n
        for row in grid:
            for v in row:
                if v == 0:
                    ans -= 1

        ans += sum(map(max, list(zip(*grid))))
        ans += sum(map(max, grid))
        return ans
        # ans = 0
        # import numpy as np
        # grid_array = np.array(grid)
        # # area of the projection onto yz plane
        # ans += sum(np.max(grid_array, axis=0))
        # # area of the projection onto xz plane
        # ans += sum(np.max(grid_array, axis=1))
        # # area of the projection onto xy plane
        # ans += sum(np.count_nonzero(grid_array, axis=0))
        #
        # return ans


s = Solution()
grid = [[1,2],[3,4]]
print(s.projectionArea(grid))

# print(sum(v for row in grid for v in row if v > 0))
# print(max)
