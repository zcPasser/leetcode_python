class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            ans += max(prices[i] - prices[i - 1], 0)

        return ans