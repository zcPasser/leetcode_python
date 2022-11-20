

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        len_s = len(s)
        # s = list(s)
        for i in range(0, len_s, 2 * k):
            if (i + k) <= len_s:
                s = s[:i] + s[i: i + k:][::-1] + s[i + k:]
            else:
                s = s[:i] + s[i:][::-1]
        return s


s = "abcdefg"
k = 2
ss = Solution()
print(ss.reverseStr(s, k))