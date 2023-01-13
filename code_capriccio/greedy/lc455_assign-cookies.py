class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        ans = 0
        g.sort()
        s.sort()
        i, j = len(g) - 1, len(s) - 1
        while i > -1 and j > -1:
            if s[j] >= g[i]:
                ans += 1
                j -= 1
            i -= 1

        return ans


g = [1,2,3]
s = [1,1]
ss = Solution()
print(ss.findContentChildren(g, s))