class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        len_nums = len(nums)
        if len_nums < 2:
            return len_nums
        dp = [1 for _ in range(len_nums)]
        ans = 1
        for i in range(1, len_nums):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            ans = max(ans, dp[i])
        return ans