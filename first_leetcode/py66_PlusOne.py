#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py66_PlusOne.py
# @Time      :2022/2/20 12:35
# @Author    :zhangcai

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        len_digits = len(digits)
        carry = 1
        for i in range(-1, -len_digits - 1, -1):
            digits[i] += carry
            if digits[i] >= 10:
                carry = digits[i] // 10
                digits[i] %= 10
            else:
                carry = 0
        if carry != 0:
            digits.insert(0, carry)

        return digits


def main():
    s = Solution()
    digits = [9]
    print(s.plusOne(digits))
    return


if __name__ == "__main__":
    main()