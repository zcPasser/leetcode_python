class Solution:
    def reverse(self, nums, start, end):
        if not nums or start >= end:
            return
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return

    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        for i in range(len_nums - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            for j in range(len_nums - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    self.reverse(nums, i + 1, len_nums - 1)
                    return
        self.reverse(nums, 0, len_nums - 1)
