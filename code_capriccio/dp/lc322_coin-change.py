import sys

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        len_coins = len(coins)
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for i in range(len_coins):
            for j in range(coins[i], amount + 1):
                if dp[j - coins[i]] != sys.maxsize:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1