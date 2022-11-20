#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py69_TheSquareRootOfX.py
# @Time      :2022/2/20 14:33
# @Author    :zhangcai

import math
class Solution:
    # def mySqrt(self, x: int) -> int:
    #     return math.floor(math.sqrt(x))

    # 二分法
    def mySqrt(self, x: int) -> int:
        left, right, res = 0, x, -1
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 <= x:
                res = mid
                left = mid + 1
            else:
                right = mid - 1

        return res

def main():
    return


if __name__ == "__main__":
    main()