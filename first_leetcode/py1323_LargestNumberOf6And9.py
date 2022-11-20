'''

'''

'''
    思路：
        1、找到 是'6' 的一位 进行翻转。
        2、字符串处理。
        3、从高位进行匹配， 即从左往右。
'''


def maximum69Number(num):
    # 边界
    # if num < 1:
    #     return 0

    num_str = str(num)
    # index_of_6 = num_str.find('6')
    # if index_of_6 == -1:
    #     return num

    return int(num_str.replace('6', '9', 1))

if __name__ == '__main__':
    print(maximum69Number(9999))


