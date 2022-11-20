"""
1、给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。
2、reshape重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。

返回：
    如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。
"""


class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        if (m * n) != (r * c):
            return mat
        mat_ = [[0] * c for _ in range(r)]

        for x in range(m * n):
            mat_[x // c][x % c] = mat[x // n][x % n]
        # for i_ in range(r):
        #     for j_ in range(c):
        #         if j == n:
        #             i, j = i + 1, 0
        #         mat_[i_][j_] = mat[i][j]
        #         j += 1

        return mat_


mat = [[1, 2], [3, 4]]
r, c = 1, 4
s = Solution()
print(s.matrixReshape(mat, r, c))