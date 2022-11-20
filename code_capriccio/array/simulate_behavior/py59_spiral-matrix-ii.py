
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = [[0] * n for _ in range(n)]
        loop = n // 2
        start_x, start_y = 0, 0
        value = 1
        for offset in range(1, loop + 1):
            for i in range(start_y, n - offset):
                ans[start_x][i] = value
                value += 1
            for i in range(start_x, n - offset):
                ans[i][n - offset] = value
                value += 1
            for i in range(n - offset, start_y, -1):
                ans[n - offset][i] = value
                value += 1
            for i in range(n - offset, start_x, -1):
                ans[i][start_y] = value
                value += 1
            start_x += 1
            start_y += 1

        if n % 2 == 1:
            mid = n // 2
            ans[mid][mid] = value

        return ans


n = 2
s = Solution()
print(s.generateMatrix(n))


