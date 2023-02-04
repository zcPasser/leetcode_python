class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        len_cost = len(cost)
        dp = [0] * (len_cost + 1)
        for i in range(2, len_cost + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]