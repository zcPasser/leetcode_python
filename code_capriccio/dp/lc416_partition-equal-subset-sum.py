class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        len_nums = len(nums)
        target = sum(nums)
        if target % 2 == 1:
            return False
        target //= 2
        dp = [0] * 10001
        for i in range(len_nums):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return dp[target] == target
