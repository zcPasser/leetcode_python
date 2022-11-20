import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        cnt = collections.defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for ch in s:
                letters[ord(ch) - ord('a')] += 1
            cnt[tuple(letters)].append(s)

        return list(cnt.values())
    # def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    #     cnt = dict()
    #     for s in strs:
    #         ss = "".join(sorted(s))
    #         if ss in cnt:
    #             cnt[ss].append(s)
    #         else:
    #             cnt[ss] = [s]
    #
    #     return [v for v in cnt.values()]


strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
print(s.groupAnagrams(strs))