class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        len_nums = len(nums)
        odd_idx = 1
        for i in range(0, len_nums, 2):
            if nums[i] % 2 == 1:
                while odd_idx < len_nums and nums[odd_idx] % 2 == 1:
                    odd_idx += 2
                nums[i], nums[odd_idx] = nums[odd_idx], nums[i]
        return nums