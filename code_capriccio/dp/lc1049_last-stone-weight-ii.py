class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        len_stones = len(stones)
        sum_stones = sum(stones)
        target = sum_stones // 2
        dp = [0] * (target + 1)
        for i in range(len_stones):
            for j in range(target, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])

        return sum_stones - dp[target] - dp[target]