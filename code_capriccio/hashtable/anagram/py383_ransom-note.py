import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_magazine = collections.Counter(magazine)

        for ch in ransomNote:
            cnt_magazine[ch] -= 1
            if cnt_magazine[ch] < 0:
                return False

        return True
