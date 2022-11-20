"""
给你一个整数数组nums 和一个整数k ，判断数组中是否存在两个 不同的索引i和j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。
如果存在，返回 true ；否则，返回 false 。

"""


class Solution:
    # 滑动窗口
    # 维护一个 大小不超过 k 的 窗口。
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s = set()
        for i, num in enumerate(nums):
            if i > k:
                s.remove(nums[i - k - 1])
            if num in s:
                return True
            s.add(num)
        return False

    # 哈希。
    # def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    #     nums_dict = {}
    #     nums_len = len(nums)
    #     for i in range(nums_len):
    #         if nums[i] not in nums_dict or (i - nums_dict[nums[i]]) > k:
    #             nums_dict[nums[i]] = i
    #         else:
    #             return True
    #
    #     return False
    # 自定义数据结构。
    # def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
    #     nums_dict = {}
    #     nums_len = len(nums)
    #     for i in range(nums_len):
    #         if nums[i] not in nums_dict:
    #             nums_dict[nums[i]] = [i, ]
    #         else:
    #             nums_dict[nums[i]].append(i)
    #     for num, v_list in nums_dict.items():
    #         v_len = len(v_list)
    #         if v_len > 1:
    #             for i in range(1, v_len):
    #                 if (v_list[i] - v_list[i - 1]) <= k:
    #                     return True
    #
    #     return False
