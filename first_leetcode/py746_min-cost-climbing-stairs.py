"""
1、一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。
2、可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

返回：
    计算并返回达到楼梯顶部的最低花费。
"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for idx in range(2, n + 1, 1):
            dp[idx] = min(dp[idx - 1] + cost[idx - 1], dp[idx - 2] + cost[idx - 2])

        return dp[n]