"""
1、长度为 2n 的整数数组 nums。
2、分成 n 对, 例如 (a1, b1)，使得从 1 到 n 的 min(ai, bi) 总和最大

返回：
    最大总和 。
"""


class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[::2])
