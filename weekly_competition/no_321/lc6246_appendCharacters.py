from collections import Counter
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        i, j = 0, 0
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                j += 1
            i += 1
        return len_t - j
