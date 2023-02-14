class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fast, slow = 0, 0
        len_nums = len(nums)
        while fast < len_nums:
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        for i in range(slow, len_nums):
            nums[i] = 0
