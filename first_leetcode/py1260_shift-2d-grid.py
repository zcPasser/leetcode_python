

class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        sum_nums = m * n
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = (i * n + j + k) % sum_nums
                ans[idx // n][idx % n] = grid[i][j]

        return ans
        # for _ in range(k):
        #     last_col = [grid[i][n - 1] for i in range(m)]
        #     if n != 1:
        #         for i in range(m):
        #             for j in reversed(range(1, n)):
        #                 grid[i][j] = grid[i][j - 1]
        #     grid[0][0] = last_col[-1]
        #     for idx in range(m - 1):
        #         grid[idx + 1][0] = last_col[idx]
        #
        # return grid


grid = [[1],[2],[3],[4],[7],[6],[5]]
k = 23
s = Solution()
print(s.shiftGrid(grid, k))
