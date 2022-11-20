'''
    leetcode-1281-The difference between the sum of the products of the integers
'''

'''
    思路：
        1、转为字符串，再用 list 存储 值。
        2、对 每个字符 做 累加 和 累乘。
        3、做差。
'''


def subtractProductAndSum(n):
    # 边界

    # 转为字符串
    data_list = [int(ch) for ch in str(n)]

    # 累乘 初始值 1
    products = 1
    for i in data_list:
        products *= i
    return products - sum(data_list)

if __name__ == '__main__':
    print(subtractProductAndSum(234))