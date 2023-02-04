class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        len_nums = len(nums)
        ans = 0
        if len_nums == 0:
            return ans
        dp = [0 for _ in range(len_nums)]
        dp[0] = nums[0]
        ans = nums[0]
        for i in range(1, len_nums):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            ans = max(ans, dp[i])
        return ans