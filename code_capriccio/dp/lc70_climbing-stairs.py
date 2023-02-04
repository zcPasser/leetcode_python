class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n + 1):
            for j in range(1, 3):
                if i - j >= 0:
                    dp[i] += dp[i - j]
        return dp[n]
    # def climbStairs(self, n: int) -> int:
    #     if n < 3:
    #         return n
    #     dp = [0] * (n + 1)
    #     dp[1], dp[2] = 1, 2
    #     for i in range(3, n + 1):
    #         # 优化：在空间上优化，只依赖于前两个状态，故只用两个变量。
    #         dp[i] = dp[i - 1] + dp[i - 2]
    #
    #     return dp[n]