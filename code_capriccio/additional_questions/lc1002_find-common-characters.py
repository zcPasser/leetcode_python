class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        ch_to_nums = [0] * 26
        len_words = len(words)
        ans = []
        if len_words < 1:
            return ans
        for ch in words[0]:
            idx = ord(ch) - ord('a')
            ch_to_nums[idx] += 1
        for i in range(1, len_words):
            ch_to_nums2 = [0] * 26
            for ch in words[i]:
                idx = ord(ch) - ord('a')
                ch_to_nums2[idx] += 1
            for j in range(26):
                ch_to_nums[j] = min(ch_to_nums[j], ch_to_nums2[j])

        for i in range(26):
            while ch_to_nums[i] > 0:
                ans.append(chr(i + ord('a')))
                ch_to_nums[i] -= 1
        return ans