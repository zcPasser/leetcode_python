import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return []
        cnt_p = [0] * 26
        cnt_s = [0] * 26
        for i in range(len_p):
            cnt_p[ord(p[i]) - 97] += 1
            cnt_s[ord(s[i]) - 97] += 1

        ans = []
        if cnt_p == cnt_s:
            ans.append(0)

        for i in range(len_s - len_p):
            cnt_s[ord(s[i]) - 97] -= 1
            cnt_s[ord(s[i + len_p]) - 97] += 1

            if cnt_p == cnt_s:
                ans.append(i + 1)
        return ans

    # def findAnagrams(self, s: str, p: str) -> list[int]:
    #     ans = []
    #     cnt_p = [0] * 26
    #     for ch in p:
    #         cnt_p[ord(ch) - ord('a')] += 1
    #     cnt_p_s = str(cnt_p)
    #     len_p = len(p)
    #     len_s = len(s)
    #     start, end = 0, len_p - 1
    #     while end < len_s:
    #         if s[end] not in p:
    #             start = end + 1
    #             end = start + len_p - 1
    #             continue
    #
    #         cnt_cur = [0] * 26
    #         for ch in s[start: end + 1]:
    #             cnt_cur[ord(ch) - ord('a')] += 1
    #         if str(cnt_cur) == cnt_p_s:
    #             ans.append(start)
    #
    #         start += 1
    #         end = start + len_p - 1
    #
    #     return ans


s = "abab"
p = "ab"
ss = Solution()
print(ss.findAnagrams(s, p))
