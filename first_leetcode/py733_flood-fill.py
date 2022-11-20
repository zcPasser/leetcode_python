"""
1、将给定的二维数组中指定的「色块」染成另一种颜色。「色块」的定义是：直接或间接相邻的同色方格构成的整体。

返回：
    染色后的图片。
"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # BFS
        old_color = image[sr][sc]
        if old_color == color:
            return image

        m, n = len(image), len(image[0])
        que = [(sr, sc)]
        while que:
            x, y = que.pop(0)
            if image[x][y] == old_color:
                image[x][y] = color

                for x_, y_ in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= x_ < m and 0 <= y_ < n and image[x_][y_] == old_color:
                        que.append((x_, y_))
        return image
        # m, n = len(image), len(image[0])
        # old_color = image[sr][sc]
        #
        # def dfs(r: int, c: int):
        #     if image[r][c] == old_color:
        #         image[r][c] = color
        #         for x_, y_ in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        #             if 0 <= x_ < m and 0 <= y_ < n and image[x_][y_] == old_color:
        #                 dfs(x_, y_)
        #
        # if color != old_color:
        #     dfs(sr, sc,)
        #
        # return image


image = [[1,1,1],[1,1,0],[1,0,1]]
r = 1
c = 1
color = 2
s = Solution()
print(s.floodFill(image, r, c, color))
