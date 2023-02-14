class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        sorted_nums = sorted(nums)
        val_map_idx = dict()
        for i in range(len_nums - 1, -1, -1):
            val_map_idx[sorted_nums[i]] = i
        ans = []
        for i in range(len_nums):
            ans.append(val_map_idx[nums[i]])
        return ans
