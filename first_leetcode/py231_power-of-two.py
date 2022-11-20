"""
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得n == 2x ，则认为 n 是 2 的幂次方。

"""


class Solution:
    # 位运算：2的幂，且为 正整数，其 2进制表示 只有1个 ‘1’。
    # 思路：最低位的1 去除后，为 ‘0’。
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1) == 0)