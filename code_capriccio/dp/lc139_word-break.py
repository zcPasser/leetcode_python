class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        len_s = len(s)
        dp = [False] * (len_s + 1)
        dp[0] = True
        for i in range(1, len_s + 1):
            for word in wordDict:
                len_word = len(word)
                if i >= len_word:
                    dp[i] = dp[i] or (dp[i - len_word] and s[i - len_word: i] == word)
        return dp[len_s]
