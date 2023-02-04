class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len_text1, len_text2 = len(text1), len(text2)
        if len_text1 == 0 or len_text2 == 0:
            return 0
        dp = [[0 for _ in range(len_text2 + 1)] for _ in range(len_text1 + 1)]

        for i in range(1, len_text1 + 1):
            for j in range(1, len_text2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[len_text1][len_text2]