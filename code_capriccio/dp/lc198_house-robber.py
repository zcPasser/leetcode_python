class Solution:
    def rob(self, nums: list[int]) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        if len_nums == 1:
            return nums[0]
        dp = [0] * len_nums
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len_nums):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]