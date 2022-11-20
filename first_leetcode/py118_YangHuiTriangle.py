'''
    leetcode-118-Yang Hui Triangle
'''
'''
    思路：
        1、
'''


def generate(numRows):
    if numRows < 1:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    res = [[1], [1, 1]]
    for i in range(3, numRows + 1):
        # 第i 层
        last_layer = res[-1]
        current_layer = [1, 1]
        # 第i层 增加 i-2 个数
        for j in range(i - 2):
            current_layer.insert(j + 1, sum(last_layer[j: j + 2]))
        res.append(current_layer)

    return res