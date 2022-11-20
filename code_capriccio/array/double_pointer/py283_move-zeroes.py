

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow_idx, fast_idx = 0, 0
        len_nums = len(nums)
        while fast_idx < len_nums:
            if nums[fast_idx] != 0:
                nums[slow_idx], nums[fast_idx] = nums[fast_idx], nums[slow_idx]
                slow_idx += 1
            fast_idx += 1



nums = [0, 1, 0]
s = Solution()
print(nums)
s.moveZeroes(nums)
print(nums)