#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py9_PalindromicNumber.py
# @Time      :2022/2/16 14:06
# @Author    :zhangcai

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return x >= 0 and s == s[::-1]


def main():
    return


if __name__ == "__main__":
    main()