"""
1、一个未经排序的整数数组，找到最长且 连续递增的子序列，并返回该序列的长度。
2、连续递增的子序列
    可以由两个下标 l 和 r（l < r）确定，如果对于每个 l <= i < r，都有 nums[i] < nums[i + 1] ，
    那么子序列 [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] 就是连续递增子序列。


返回：
    最长连续递增的子序列长度。
"""


class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        len_of_nums, len_of_window = len(nums), 1
        cur_idx = 0
        next_idx = cur_idx + len_of_window
        is_legal = True
        while next_idx < len_of_nums:
            if nums[next_idx] > nums[next_idx - 1]:
                if not is_legal:
                    j = cur_idx
                    is_legal = True
                    while j < next_idx - 1:
                        if nums[j] < nums[j + 1]:
                            j += 1
                        else:
                            is_legal = False
                            cur_idx = j + 1
                            break
                else:
                    len_of_window += 1
            else:
                is_legal = False
                cur_idx = next_idx

            next_idx = cur_idx + len_of_window

        return len_of_window


nums = [1,3,5,4,2,3,4]
s = Solution()
print(s.findLengthOfLCIS(nums))