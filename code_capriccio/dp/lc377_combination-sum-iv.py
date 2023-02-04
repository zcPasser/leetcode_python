class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(0, target + 1):
            for j in range(len_nums):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]

        return dp[target]
