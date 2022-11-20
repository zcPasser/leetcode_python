#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py1_sumOfTwoNumbers.py
# @Time      :2022/2/13 14:05
# @Author    :zhangcai

# 给定一个整数数组 nums 和一个整数目标值 target，
# 请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

# 示例 1：
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         len_nums = len(nums)
#         for i in range(len_nums):
#             for j in range(i + 1, len_nums):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []
#
#     def twoSum2(self, nums: list[int], target: int) -> list[int]:
#         hashtable = dict()
#         for i, num in enumerate(nums):
#             if target - num in hashtable:
#                 return [hashtable[target - num], i]
#             hashtable[nums[i]] = i
#         return []

def main():
    import math
    print('sa{0}'.format(math.sin(math.pi/6)))
    return


if __name__ == "__main__":
    main()