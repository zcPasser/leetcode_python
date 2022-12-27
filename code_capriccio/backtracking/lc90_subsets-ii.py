class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.used = []
        self.len_nums = 0

    def backtracking(self, nums: list[int], start_idx: int):
        self.ans.append(self.path[:])
        if start_idx >= self.len_nums:
            return
        for i in range(start_idx, self.len_nums):
            if i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]:
                continue
            self.used[i] = True
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.used[i] = False
            self.path.pop()

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.len_nums = len(nums)
        self.used = [False] * self.len_nums
        self.ans.clear()
        self.path.clear()
        nums.sort()
        self.backtracking(nums, 0)
        return self.ans

nums = [1,2,2]
s = Solution()
print(s.subsetsWithDup(nums))