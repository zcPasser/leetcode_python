"""
丑数 就是只包含质因数 2、3 和 5 的正整数。

给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
"""
import math


class Solution:
    def isUgly(self, n: int) -> bool:
        while True:
            if n == 1:
                return True
            elif n < 1:
                return False
            elif n % 2 == 0:
                n /= 2
            elif n % 3 == 0:
                n /= 3
            elif n % 5 == 0:
                n /= 5
            else:
                return False
