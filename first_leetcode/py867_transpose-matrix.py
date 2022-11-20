


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        import numpy as np
        return np.transpose(matrix).tolist()
        # m, n = len(matrix), len(matrix[0])
        # ans = [[0] * m for _ in range(n)]
        # for i in range(n):
        #     for j in range(m):
        #         ans[i][j] = matrix[j][i]
        #
        # return ans
