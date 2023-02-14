class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        ans = 0
        len_s = len(s)
        if len_s < 1:
            return ans
        for i in range(len_s):
            if s[i] == 'L':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                ans += 1
        return ans