class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        len_prices = len(prices)
        dp = [[0, 0, 0, 0, 0] for _ in range(len_prices)]
        dp[0] = [0, -prices[0], 0, -prices[0], 0]
        for i in range(1, len_prices):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        return max(dp[len_prices - 1][2], dp[len_prices - 1][4])