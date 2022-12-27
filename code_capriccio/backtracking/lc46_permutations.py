class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.used = None
        self.len_nums = 0

    def backtracking(self, nums: list[int]):
        if len(self.path) == self.len_nums:
            self.ans.append(self.path[:])
            return
        for i in range(self.len_nums):
            if self.used[i]:
                continue
            self.used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums)
            self.used[i] = False
            self.path.pop()

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.ans.clear()
        self.path.clear()
        self.len_nums = len(nums)
        self.used = [False] * self.len_nums
        self.backtracking(nums)
        return self.ans

