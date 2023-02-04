class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        len_prices = len(prices)
        dp = [[0, 0] for _ in range(len_prices)]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, len_prices):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
        return dp[len_prices - 1][1]