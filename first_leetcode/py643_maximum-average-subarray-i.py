"""
1、一个由 n 个元素组成的整数数组 nums 和一个整数 k 。
2、找出平均数最大且 长度为 k 的连续子数组。

返回：
    输出该最大平均数。
"""
import sys


class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n = len(nums)
        temp_total = max_total = sum(nums[: k])
        for i in range(k, n):
            temp_total = temp_total - nums[i - k] + nums[i]
            max_total = max(temp_total, max_total)

        return max_total / k


s = Solution()
nums = [0,4,0,3,2]
k = 1
print(s.findMaxAverage(nums, k))