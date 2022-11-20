import collections


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> list[list[int]]:
        ans = []
        is_visited = [[False] * cols for _ in range(rows)]
        que = collections.deque([(rCenter, cCenter)])
        cnt = 0
        while cnt < rows * cols:
            x, y = que.popleft()
            if x == -1 or x == rows or y == -1 or y == cols or is_visited[x][y]:
                continue
            is_visited[x][y] = True
            ans.append([x, y])
            cnt += 1
            for r, c in [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]]:
                if r == -1 or r == rows or c == -1 or c == cols or is_visited[r][c]:
                    continue
                que.append([r, c])

        return ans
        # cnt = {}
        # for i in range(rows):
        #     for j in range(cols):
        #         dist = abs(rCenter - i) + abs(cCenter - j)
        #         if dist in cnt:
        #             cnt[dist].append([i, j])
        #         else:
        #             cnt[dist] = [[i, j]]
        #
        # max_d = max(rCenter + cCenter, rCenter + cols - cCenter - 1, rows - 1 - rCenter + cols - 1 - cCenter,
        #             rows - 1 - rCenter + cCenter)
        # ans = []
        # for d in range(max_d + 1):
        #     ans.extend(cnt[d])
        #
        # return ans

        # ans = [[rCenter, cCenter]]
        #
        # max_d = max(rCenter + cCenter, rCenter + cols - cCenter - 1, rows - 1 - rCenter + cols - 1 - cCenter, rows - 1 - rCenter + cCenter)
        # for d in range(1, max_d + 1):
        #     x, y = rCenter, cCenter - d
        #     while x > rCenter - d:
        #         if 0 <= x < rows and 0 <= y < cols:
        #             ans.append([x, y])
        #         x -= 1
        #         y += 1
        #
        #     x, y = rCenter - d, cCenter
        #     while x < rCenter:
        #         if 0 <= x < rows and 0 <= y < cols:
        #             ans.append([x, y])
        #         x += 1
        #         y += 1
        #
        #     x, y = rCenter, cCenter + d
        #     while x <= rCenter + d:
        #         if 0 <= x < rows and 0 <= y < cols:
        #             ans.append([x, y])
        #         x += 1
        #         y -= 1
        #
        #     x, y = rCenter + d, cCenter
        #     while x >= cCenter:
        #         if 0 <= x < rows and 0 <= y < cols:
        #             ans.append([x, y])
        #         x -= 1
        #         y -= 1
        #
        # return ans


rows = 3
cols = 3
rCenter = 0
cCenter = 2
s = Solution()
print(s.allCellsDistOrder(rows, cols, rCenter, cCenter))
# [[0,2],[0,1],[1,2],[0,0],[1,1],[2,2],[1,0],[2,1],[2,0]]