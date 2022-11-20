"""
description:
    1、an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

return:
    any array that satisfies this condition.
"""
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        len_of_nums = len(nums)
        idx_of_odd, idx_of_even = 0, len_of_nums - 1

        while idx_of_odd < idx_of_even:
            while idx_of_odd < len_of_nums and nums[idx_of_odd] % 2 != 1:
                idx_of_odd += 1
            while idx_of_even >= 0 and nums[idx_of_even] % 2 != 0:
                idx_of_even -= 1
            if idx_of_odd < idx_of_even:
                nums[idx_of_odd], nums[idx_of_even] = nums[idx_of_even], nums[idx_of_odd]

        return nums

nums = [0,2]
s = Solution()
print(s.sortArrayByParity(nums))
