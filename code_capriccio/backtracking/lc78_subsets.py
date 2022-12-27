class Solution:
    def __init__(self):
        self.ans = []
        self.path = []

    def backtracking(self, nums: list[int], start_idx: int):
        len_nums = len(nums)
        self.ans.append(self.path[:])
        if start_idx >= len_nums:
            return
        for i in range(start_idx, len_nums):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()

    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.path.clear()
        self.ans.clear()
        self.backtracking(nums, 0)
        return self.ans
