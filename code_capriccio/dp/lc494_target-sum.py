class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        sum_nums = sum(nums)
        len_nums = len(nums)
        if abs(target) > sum_nums or ((target + sum_nums) % 2 != 0):
            return 0
        bag_size = (target + sum_nums) // 2
        dp = [0] * (bag_size + 1)
        dp[0] = 1
        for i in range(len_nums):
            for j in range(bag_size, nums[i] - 1, -1):
                dp[j] += dp[j - nums[i]]

        return dp[bag_size]