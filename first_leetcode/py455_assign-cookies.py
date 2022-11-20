class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s = sorted(s)
        g = sorted(g)
        len1, len2 = len(g), len(s)
        ans = 0
        i, j = 0, 0
        while True:
              if i == len1 or j == len2:
                 break
              if g[i] <= s[j]:
                 ans += 1
                 i, j = i + 1, j + 1
              else:
                 j += 1
        return ans