"""
1、和谐数组是指一个数组里元素的最大值和最小值之间的差别 正好是 1 。
2、整数数组 nums ，请你在所有可能的子序列中找到最长的和谐子序列的长度。
3、数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

返回：
    满足条件的最长和谐子序列的长度。
"""
from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        num_to_count = Counter(nums)

        return max((v + num_to_count[k + 1] for k, v in num_to_count.items() if k + 1 in num_to_count), default=0)

s = Solution()
nums = [1,2,3,4]
print(s.findLHS(nums))
