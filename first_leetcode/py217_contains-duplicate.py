"""
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
"""


class Solution:
    # 去重，哈希。
    def containsDuplicate(self, nums: list[int]) -> bool:
        # return len(set(nums)) != len(nums)
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False