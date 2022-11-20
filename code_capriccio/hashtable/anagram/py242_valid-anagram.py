import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = collections.Counter(s)
        for ch in t:
            cnt_s[ch] -= 1
            if cnt_s[ch] < 0:
                return False
            elif cnt_s[ch] == 0:
                cnt_s.pop(ch)

        return len(cnt_s) == 0


s = "ab"
t = "a"
ss = Solution()
print(ss.isAnagram(s, t))