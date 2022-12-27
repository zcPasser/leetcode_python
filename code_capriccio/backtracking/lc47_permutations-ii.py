class Solution:
    def __init__(self):
        self.ans = []
        self.path = []
        self.len_nums = 0
        self.used = None

    def backtracking(self, nums: list[int]):
        if len(self.path) == self.len_nums:
            self.ans.append(self.path[:])
            return
        for i in range(self.len_nums):
            if self.used[i] or (i > 0 and nums[i] == nums[i - 1] and not self.used[i - 1]):
                continue
            self.path.append(nums[i])
            self.used[i] = True
            self.backtracking(nums)
            self.path.pop()
            self.used[i] = False

    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        self.ans.clear()
        self.path.clear()
        self.len_nums = len(nums)
        self.used = [False] * self.len_nums
        nums.sort()
        self.backtracking(nums)
        return self.ans

nums = [1,1,2]
s = Solution()
print(s.permuteUnique(nums))