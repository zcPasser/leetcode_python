class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        len_prices = len(prices)
        if len_prices == 0:
            return 0
        dp = [[0 for _ in range(2 * k + 1)] for _ in range(len_prices)]
        for i in range(1, 2 * k + 1, 2):
            dp[0][i] = -prices[0]
        for i in range(1, len_prices):
            for j in range(0, 2 * k - 1, 2):
                dp[i][j + 1] = max(dp[i - 1][j + 1], dp[i - 1][j] - prices[i])
                dp[i][j + 2] = max(dp[i - 1][j + 2], dp[i - 1][j + 1] + prices[i])

        return dp[len_prices - 1][2 * k]