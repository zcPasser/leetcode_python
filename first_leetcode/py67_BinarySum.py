#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py67_BinarySum.py
# @Time      :2022/2/20 13:10
# @Author    :zhangcai

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # a_bin = int(a, 2)
        # b_bin = int(b, 2)
        #
        # return str(bin(a_bin + b_bin))[2:]
        return '{0:b}'.format(int(a, 2) + int(b, 2))

def main():
    a = "11"
    b = "1"
    s = Solution()
    print(s.addBinary(a, b))
    return


if __name__ == "__main__":
    main()