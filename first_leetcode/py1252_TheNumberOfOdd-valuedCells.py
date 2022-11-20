'''
    leetcode-1252-the number of odd-valued cells
'''
'''
    思路：
        1、初始化矩阵。
        2、对索引 列表 逐项操作。
'''
def oddCells(m, n, indices):
    # 初始化 矩阵
    matrix = [[0] * n for i in range(m)]
    for item in indices:
        # 对 row操作
        matrix[item[0]] = [i + 1 for i in matrix[item[0]]]
        # 对 列 操作
        for i in range(m):
            matrix[i][item[1]] += 1
    # 统计 奇数 个数
    count = 0
    for i in range(m):
        for j in range(n):
            count = count + 1 if matrix[i][j] % 2 == 1 else count

    return count