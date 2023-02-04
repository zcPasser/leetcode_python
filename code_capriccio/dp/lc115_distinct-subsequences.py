class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return 0
        dp = [[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)]
        for i in range(len_s + 1):
            dp[i][0] = 1
        for i in range(1, len_s + 1):
            for j in range(1, len_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]