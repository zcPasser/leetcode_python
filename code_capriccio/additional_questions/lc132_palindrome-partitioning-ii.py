class Solution:
    def minCut(self, s: str) -> int:
        len_s = len(s)
        if len_s < 2:
            return 0

        is_palindromic = [[False for _ in range(len_s)] for _ in range(len_s)]

        for i in range(len_s - 1, -1, -1):
            for j in range(i, len_s):
                if s[i] == s[j]:
                    if j - i < 2:
                        is_palindromic[i][j] = True
                    else:
                        is_palindromic[i][j] = is_palindromic[i + 1][j - 1]

        dp = [i for i in range(len_s)]
        for i in range(1, len_s):
            if is_palindromic[0][i]:
                dp[i] = 0
                continue
            for j in range(i):
                if is_palindromic[j + 1][i]:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
