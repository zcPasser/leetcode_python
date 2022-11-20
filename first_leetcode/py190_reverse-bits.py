"""
颠倒给定的 32 位无符号整数的二进制位。
"""


class Solution:
    # 位运算。
    def reverseBits(self, n: int) -> int:
        n = n
        res = 0
        for i in range(32):
            res = res << 1
            res += n & 1
            n = n >> 1
        return res
    # 字符串处理。
    # def reverseBits(self, n: int) -> int:
    #     num_str = str(bin(n))
    #     str_len = len(num_str)
    #     reverse_num_str = num_str[-1:1:-1]
    #     if str_len < 34:
    #         for i in range(34 - str_len):
    #             reverse_num_str += '0'
    #     res = 0
    #     for i, ch in enumerate(reverse_num_str[::-1]):
    #         num = ord(ch) - ord('0')
    #         res += num * pow(2, i) if num > 0 else 0
    #     print(num_str)
    #     print(reverse_num_str)
    #     return res


ss = Solution()
num = 0b00000010100101000001111010011100
print(ss.reverseBits(num))

