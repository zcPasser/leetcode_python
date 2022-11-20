#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py53_TheLargestSubarraySum.py
# @Time      :2022/2/20 9:51
# @Author    :zhangcai

class Solution:


    # 超时
    # def maxSubArray(self, nums: list[int]) -> int:
    #     len_nums, low, high, res = len(nums), -1, len(nums) - 1, sum(nums)
    #     len_sliding_interval = len_nums - 1
    #
    #     while len_sliding_interval >= 1:
    #         # 更新 滑动区间的 左端 和 右端
    #         low += 1
    #         high = low + len_sliding_interval - 1
    #         if high < len_nums:
    #             # 合法 滑动区间
    #             temp = sum(nums[low : high + 1])
    #             # 更新 最大和
    #             res = temp if temp > res else res
    #         else:
    #             # 非法 滑动区间，已溢出，缩短 滑动区间 的 长度
    #             len_sliding_interval -= 1
    #             low = -1
    #
    #     return res

    # 获取 以nums[index] 结尾的 最大连续子序列 和
    def get_dp(self, nums: list[int], index) -> int:
        res = nums[index]


        return res

    def maxSubArray(self, nums: list[int]) -> int:
        dp = [nums[0]]
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        # 创建 dp 状态数组
        for i in range(1, len_nums):
            if dp[i - 1] <= 0:
                dp.append(nums[i])
            else:
                dp.append(dp[i - 1] + nums[i])

        return max(dp)


def main():
    s = Solution()
    nums = [1,-1,-2]
    print(s.maxSubArray(nums))
    return


if __name__ == "__main__":
    main()