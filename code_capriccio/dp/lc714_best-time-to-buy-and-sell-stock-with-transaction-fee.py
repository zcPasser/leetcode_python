class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        len_prices = len(prices)
        if len_prices == 0:
            return 0
        dp = [[0, 0] for _ in range(len_prices)]
        dp[0][0] = -prices[0]
        for i in range(1, len_prices):
            dp[i][0] = max(dp[i - 1][1] - prices[i], dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][0] + prices[i] - fee, dp[i - 1][1])

        return max(dp[len_prices - 1])