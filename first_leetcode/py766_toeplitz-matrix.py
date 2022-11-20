

class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])

        for i in range(len(matrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True

        # for i in range(1, m):
        #     for j in range(1, n):
        #         if matrix[i][j] != matrix[i - 1][j - 1]:
        #             return False


        # for j in range(n):
        #     idx_r, idx_c = 0, j
        #     while idx_r < m - 1 and idx_c < n - 1:
        #         if matrix[idx_r][idx_c] != matrix[idx_r + 1][idx_c + 1]:
        #             return False
        #         idx_r += 1
        #         idx_c += 1
        #
        # for i in range(1, m):
        #     idx_r, idx_c = i, 0
        #     while idx_r < m - 1 and idx_c < n - 1:
        #         if matrix[idx_r][idx_c] != matrix[idx_r + 1][idx_c + 1]:
        #             return False
        #         idx_r += 1
        #         idx_c += 1

        return True