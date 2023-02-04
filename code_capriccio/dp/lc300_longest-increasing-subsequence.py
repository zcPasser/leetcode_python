class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        len_nums = len(nums)
        if len_nums < 2:
            return len_nums
        dp = [1 for _ in range(len_nums)]
        ans = 1
        for i in range(1, len_nums):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans