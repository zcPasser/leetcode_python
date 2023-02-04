class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        len_coins = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len_coins):
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]