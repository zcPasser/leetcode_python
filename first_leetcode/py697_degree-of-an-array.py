"""
1、一个非空且只包含非负数的整数数组 nums。
2、数组的 度 的定义是指数组里任一元素出现频数的最大值。
3、在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组。

返回：
    返回最短连续子数组的长度。
"""


class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        num_to_freq_and_start_and_end = {}

        for idx, num in enumerate(nums):
            if num not in num_to_freq_and_start_and_end:
                num_to_freq_and_start_and_end[num] = [1, idx, idx]
            else:
                num_to_freq_and_start_and_end[num][0] += 1
                num_to_freq_and_start_and_end[num][2] = idx

        degree = 1
        ans = []
        for freq, start_idx, end_idx in num_to_freq_and_start_and_end.values():
            if degree == freq:
                ans.append(end_idx - start_idx + 1)
            elif degree < freq:
                degree = freq
                ans.clear()
                ans.append(end_idx - start_idx + 1)

        return min(ans)






