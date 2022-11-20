"""
abstract:
    1、an integer array nums where the largest integer is unique.
    2、whether the largest element in the array is at least twice as much as every other number in the array。
        If it is, return the index of the largest element, or return -1 otherwise.

return:
    return the index of the largest element which is at least twice as much as every other number in the array,
    or return -1 otherwise.
"""

class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        max_num, next_largest_num, id = -1, -1, -1
        for idx, num in enumerate(nums):
            if num > max_num:
                max_num, next_largest_num, id = num, max_num, idx
            elif num > next_largest_num:
                next_largest_num = num

        return id if max_num >= 2 * next_largest_num else -1

s = Solution()
nums = [3,6,1,0]
print(s.dominantIndex(nums))