#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py70_ClimbStairs.py
# @Time      :2022/2/20 15:06
# @Author    :zhangcai

class Solution:
    # 递归 实现
    # 爬 n阶 = 爬到第 n-1 阶 + 1阶 或 爬到 n-2 阶 + 2阶
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    # 动态规划 实现
    # def climbStairs(self, n: int) -> int:
    #     nums = [1, 2]
    #     if n == 1 or n == 2:
    #         return nums[n - 1]
    #     for i in range(2, n):
    #         nums.append(nums[-1] + nums[-2])
    #
    #     return nums[-1]

    # 斐波那契而数列
    def climbStairs(self, n: int) -> int:
        nums = [1, 2 ,3]
        if n == 1 or n == 2:
            return nums[n - 1]
        for i in range(2, n):
            nums[2] = nums[0] + nums[1]
            nums[0] = nums[1]
            nums[1] = nums[2]
        return nums[1]

def main():
    s = Solution()
    ex = 2
    print(s.climbStairs(ex))
    return


if __name__ == "__main__":
    main()