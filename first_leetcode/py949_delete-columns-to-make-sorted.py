

from itertools import pairwise

class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        # return sum(any(x > y for x, y in pairwise(col)) for col in zip(*strs))
        r, c = len(strs), len(strs[0])
        ans = 0
        for j in range(c):
            for i in range(r - 1):
                if strs[i][j] > strs[i + 1][j]:
                    ans += 1
                    break

        return sum(any((x < y for x, y in pairwise(col)) for col in zip(*strs)))


strs = ["zyx","wvu","tsr"]
s = Solution()
print(s.minDeletionSize(strs))