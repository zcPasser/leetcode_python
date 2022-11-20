"""
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
"""


class Solution:
    # 数学方法：二项式系数，编号都从0开始。
    def getRow(self, rowIndex: int) -> list[int]:
        def number_of_combinations(n, m):
            if n == m:
                return 1

            def factorial(x):
                if x == 0:
                    return 1
                res = 1
                for i in range(1, x + 1):
                    res = res * i
                return res
            return factorial(n) // (factorial(m) * factorial(n - m))
        res_list = []
        for i in range(rowIndex):
            res_list.append(number_of_combinations(rowIndex, i))
        res_list.append(1)
        return res_list
    # 暴力法。
    # def getRow(self, rowIndex: int) -> list[int]:
    #     tower_list = [[1], [1, 1]]
    #     for i in range(2, rowIndex + 1):
    #         level_list = [1]
    #         last_level_list = tower_list[i - 1]
    #         for j in range(i - 1):
    #             level_list.append(last_level_list[j] + last_level_list[j + 1])
    #         level_list.append(1)
    #         tower_list.append(level_list)
    #
    #     return tower_list[rowIndex]

ss = Solution()

print(ss.getRow(3))
