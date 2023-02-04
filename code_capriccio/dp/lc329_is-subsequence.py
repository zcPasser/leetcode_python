class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s, len_t = len(s), len(t)
        if len_s > len_t:
            return False
        dp = [[0 for _ in range(len_t + 1)] for _ in range(len_s + 1)]

        for i in range(1, len_s + 1):
            for j in range(1, len_t + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]
        if dp[len_s][len_t] == len_s:
            return True
        return False
