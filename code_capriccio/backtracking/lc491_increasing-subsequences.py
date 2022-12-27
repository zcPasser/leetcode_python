class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.used = None
        self.len_nums = 0


    def backtracking(self, nums: list[int], start_idx: int):
        if len(self.path) > 1:
            self.ans.append(self.path[:])
        if start_idx >= self.len_nums:
            return
        level_visited_set = [0] * 201
        for i in range(start_idx, self.len_nums):
            # 树层去重
            if level_visited_set[nums[i] + 100] == 1:
                continue
            # 递增规则 检查
            if self.path and self.path[-1] > nums[i]:
                continue
            self.path.append(nums[i])
            level_visited_set[nums[i] + 100] = 1
            self.backtracking(nums, i + 1)
            self.path.pop()

    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        self.ans.clear()
        self.path.clear()
        self.used = [False] * 202
        self.len_nums = len(nums)
        self.backtracking(nums, 0)
        return self.ans

nums = [4,8,6,9]
s = Solution()
print(s.findSubsequences(nums))