'''

'''

'''
    思路：
        1、涉及词频统计， 使用 字典。
'''


def findSpecialInteger(arr):
    len_arr = len(arr)
    # 边界
    # if len_arr < 1:
    #     return 0

    # 词频 字典
    num_dict = {}
    for num in arr:
        num_dict[num] = num_dict.get(num, 0) + 1
    for k, v in num_dict.items():
        if float(v) > (len_arr * 0.25):
            return k
    return 0

if __name__ == '__main__':
    print(findSpecialInteger([1,2,2,6,6,6,6,7,10]))