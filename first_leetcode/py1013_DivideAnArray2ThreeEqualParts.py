'''
    leetcode-1013-Divide an array into three equal parts
'''

'''
    思路：找 切分点
        
        暴力法
        
        分治
        1、sum整体求和。
        2、将暴力法中 找2个 切分点 转为 找1个 切分点
        3、题意：sum(0-i) 和 sum(i-尾部) 有倍数关系:0.5倍 或 2倍
'''
def canThreePartsEqualSum(arr):
    sum_data = sum(arr)
    len_data = len(arr)
    # 边界考虑
    div, mod = divmod(sum_data, 3)
    if mod != 0:
        return False
    lst = []
    total = 0
    for i in range(len_data):
        total += arr[i]
        if total == div:
            lst.append(total)
            total = 0
            if len(lst) == 2 and i < len_data - 1:
                return sum(arr[i + 1:]) == div
    return False

    # 暴力法
    # i, j = 1, 2
    # sum1, sum2, sum3 = 0, 0, 0
    # len_data = len(arr)
    # for i in range(1, len_data - 1):
    #     for j in range(i + 1, len_data):
    #         sum1, sum2, sum3 = sum(arr[0: i]), sum(arr[i: j]), sum(arr[j:])
    #         if sum1 == sum2 == sum3:
    #             print(arr[0: i], arr[i: j], arr[j:])
    #             return True
    # return False

    # def split2equal(data):
    #     len_data = len(data)
    #     for i in range(1, len_data):
    #         if sum(data[0: i]) == sum(data[i:]):
    #             return True
    #     return False
    #
    # # 从整体 到 局部：分治
    # sum_data = sum(arr)
    # len_data = len(arr)
    # for i in range(len_data):
    #     sum1, sum2 = sum(arr[0: i]), sum(arr[i:])
    #     if (sum2 == sum1 * 2):
    #         print(arr[i:])
    #         return split2equal(arr[i:])
    #     if (sum1 == sum2 * 2):
    #         print(arr[0: i])
    #         return split2equal(arr[0: i])

    return False

if __name__ == '__main__':
    data_list = [29,31,27,-10,-67,22,15,-1,-16,-29,59,-18,48]
    print(canThreePartsEqualSum(data_list))