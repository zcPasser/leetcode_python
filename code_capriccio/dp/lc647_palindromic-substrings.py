class Solution:
    def countSubstrings(self, s: str) -> int:
        len_s = len(s)
        ans = 0
        dp = [[False for _ in range(len_s)] for _ in range(len_s)]
        for i in range(len_s - 1, -1, -1):
            for j in range(i, len_s):
                if s[i] == s[j]:
                    if (j - i) <= 1:
                        ans += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        ans += 1
                        dp[i][j] = True
        return ans