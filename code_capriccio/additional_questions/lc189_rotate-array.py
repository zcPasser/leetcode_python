class Solution:
    # 区间：[begin, end]
    def reverse(self, nums: list[int], begin: int, end: int) -> None:
        i, j = begin, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        k %= len_nums
        self.reverse(nums, 0, len_nums - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len_nums - 1)
