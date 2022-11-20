"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""


class Solution:
    # 暴力法。
    # def moveZeroes(self, nums: list[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     len_nums = len(nums)
    #     if len_nums == 1:
    #         return
    #
    #     p = 0
    #
    #     for i in range(len_nums):
    #         if nums[i] == 0:
    #             p = i
    #             break
    #     q = p + 1
    #     while p < len_nums and q < len_nums:
    #         if nums[p] == 0:
    #             last_q = q
    #             for i in range(q, len_nums):
    #                 if nums[i] != 0:
    #                     nums[p], nums[i] = nums[i], 0
    #                     q = i + 1
    #                     break
    #             if last_q == q:
    #                 return
    #         else:
    #             p += 1

        def moveZeroes(self, nums: list[int]) -> None:
            n = len(nums)
            left = right = 0
            while right < n:
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                right += 1


nums = [0,1,0,3,12]
print(nums)
s = Solution()
s.moveZeroes(nums)
print(nums)