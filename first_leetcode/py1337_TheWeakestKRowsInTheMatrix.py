'''

'''

'''
    思路：
        1、实则 统计问题，采用字典。
        2、对于一行，由于特性，从后往前获取1的 索引。
        3、字典存储，k:v表示 行号：last '1'索引---'0'第一次出现。
'''


def kWeakestRows(mat, k):
    m, n = len(mat), len(mat[0])
    # 边界
    # if m <2 or n < 2:
    #     return []

    count_dict = {}
    print(type(count_dict))
    for i in range(m):
        count_dict[i] = mat[i].count(0)
    count_list = sorted(count_dict.items(), key=lambda x:(-x[1], x[0]))

    lst = count_list[:k]

    return [key for key, value in lst]

if __name__ == '__main__':
    mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
    print(kWeakestRows(mat, 3))