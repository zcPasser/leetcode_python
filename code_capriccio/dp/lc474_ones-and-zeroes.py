class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for s in strs:
            one_num, zero_num = 0, 0
            for ch in s:
                if ch == '0':
                    zero_num += 1
                else:
                    one_num += 1
            for i in range(m, zero_num - 1, -1):
                for j in range(n, one_num - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero_num][j - one_num] + 1)
        return dp[m][n]


s = ["10","0001","111001","1","0"]
a = 5
b = 3
ss = Solution()
print(ss.findMaxForm(s, a, b))