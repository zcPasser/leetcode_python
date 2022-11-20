"""
给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return max(nums)
        import sys
        a, b, c = -sys.maxsize - 1, -sys.maxsize - 1, -sys.maxsize - 1
        for num in nums:
            if c < num < b:
                c = num
            elif b < num < a:
                b, c = num, b
            elif num > a:
                a, b, c = num, a, b
        return a if c == -sys.maxsize - 1 else c
