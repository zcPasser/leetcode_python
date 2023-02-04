class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0, 1]
        for _ in range(2, n + 1):
            tmp = dp[0] + dp[1]
            dp[0], dp[1] = dp[1], tmp

        return dp[1]