"""
description:
    1、An array is monotonic if it is either monotone increasing or monotone decreasing.

return:
    True if the given array is monotonic, or false otherwise.
"""


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        len_of_nums = len(nums)
        if len_of_nums == 1 or len_of_nums == 2:
            return True
        is_ascend, idx = None, 0
        while is_ascend is None and idx < len_of_nums - 1:
            if nums[idx] < nums[idx + 1]:
                is_ascend = True
            elif nums[idx] > nums[idx + 1]:
                is_ascend = False
            idx += 1

        if is_ascend is None:
            return True

        for i in range(idx + 1, len_of_nums):
            if (nums[i - 1] <= nums[i] and is_ascend) or (nums[i - 1] >= nums[i] and not is_ascend):
                continue
            else:
                return False

        return True


nums = [1,3,2]
s = Solution()
print(s.isMonotonic(nums))