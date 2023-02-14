class Solution:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.max_len = 0

    def extend(self, i: int, j: int, s: str, len_s: int):
        while i >= 0 and j < len_s and s[i] == s[j]:
            if j - i + 1 > self.max_len:
                self.left = i
                self.right = j
                self.max_len = j - i + 1
            i -= 1
            j += 1

    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        for i in range(len_s):
            self.extend(i, i, s, len_s)
            self.extend(i, i + 1, s, len_s)
        return s[self.left: self.right + 1]
    # def longestPalindrome(self, s: str) -> str:
    #     len_s = len(s)
    #     max_len = 0
    #     left, right = 0, 0
    #     dp = [[False for _ in range(len_s)] for _ in range(len_s)]
    #     for i in range(len_s - 1, -1, -1):
    #         for j in range(i, len_s):
    #             if s[i] == s[j]:
    #                 if (j - i) <= 1:
    #                     dp[i][j] = True
    #                 elif dp[i + 1][j - 1]:
    #                     dp[i][j] = True
    #
    #             if dp[i][j] and (j - i + 1) > max_len:
    #                 max_len = j - i + 1
    #                 left, right = i, j
    #     return s[left: right + 1]
