"""
abstract:
    1、a string licensePlateand an array of strings words.
        find the shortest completing word in words.
    2、A completing word is a word that contains all the letters in licensePlate.
        Ignore numbers and spaces in licensePlate, and treat letters as case insensitive.
        If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

return:
    Return the shortest completing word in words.It is guaranteed an answer exists.
    If there are multiple shortest completing words, return the first one that occurs in words.

"""

from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        letter_to_cnts = {}
        for ch in licensePlate:
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z':
                if 'A' <= ch <= 'Z':
                    ch = ch.lower()
                letter_to_cnts[ch] = letter_to_cnts.get(ch, 0) + 1
        least_len_of_target = 0
        for cnt in letter_to_cnts.values():
            least_len_of_target += cnt
        res = []
        for word in words:
            is_ans = True
            if len(word) >= least_len_of_target:
                cnt = Counter(word)
                for ch in letter_to_cnts:
                    if ch not in cnt or cnt[ch] < letter_to_cnts[ch]:
                        is_ans = False
                        break
                if is_ans:
                    res.append(word)
        ans = res[0]
        for re in res:
            if len(re) < len(ans):
                ans = re

        return ans


licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]

s = Solution()
print(s.shortestCompletingWord(licensePlate, words))
