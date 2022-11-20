"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。
"""

class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while True:
            if num < 10:
               return num
            else:
                num = sum([int(ch) for ch in s])
                s = str(num)