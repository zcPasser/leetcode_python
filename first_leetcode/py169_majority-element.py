"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 n/2 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

"""


class Solution:
    # 暴力法——枚举法：O(n^2)。

    # 哈希法——统计次数，python——字典。
    # 空间复杂度：O(n)。
    def majorityElement(self, nums: list[int]) -> int:
        len_nums = len(nums)
        hash_dict = dict()
        for num in nums:
            hash_dict[num] = hash_dict.get(num, 0) + 1
        res_k, res_v = 0, 0
        for k, v in hash_dict.items():
            if v > res_v:
                res_k, res_v = k, v

        return res_k


nums = [6,5,5]
ss = Solution()
print(ss.majorityElement(nums))