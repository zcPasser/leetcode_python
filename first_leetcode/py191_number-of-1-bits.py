"""
编写一个函数，输入是一个无符号整数（以二进制串的形式），
返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
"""


class Solution:
    # 数值转为字符串处理。
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            # n 的 第 i 位 做 &运算，判断其是否为 1。
            if n & (1 << i) != 0:
                res += 1
        return res
    # 数值转为字符串处理。
    # def hammingWeight(self, n: int) -> int:
    #     n_str = bin(n)
    #     res = 0
    #     for ch in n_str:
    #         if ch == '1':
    #             res += 1
    #     return res