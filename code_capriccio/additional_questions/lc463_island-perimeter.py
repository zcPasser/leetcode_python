class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        cover = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans += 1
                    if (i - 1) >= 0 and grid[i - 1][j] == 1:
                        cover += 1
                    if (j - 1) >= 0 and grid[i][j - 1] == 1:
                        cover += 1
        return ans * 4 - cover * 2