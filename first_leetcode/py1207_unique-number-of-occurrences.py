import collections


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        cnt = collections.Counter(arr)
        occurence_set = set(cnt.values())
        return len(occurence_set) == len(cnt.keys())


arr = [-3,0,1,-3,1,1,1,-3,10,0]
s = Solution()
print(s.uniqueOccurrences(arr))