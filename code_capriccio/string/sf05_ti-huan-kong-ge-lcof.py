

class Solution:
    def replaceSpace(self, s: str) -> str:
        ans = list(s)
        cnt = s.count(' ')
        ans.extend([''] * cnt * 2)
        # len_s = len(s)
        left, right = len(s) - 1, len(ans) - 1
        while left >= 0:
            if ans[left] == ' ':
                ans[right] = '0'
                ans[right - 1] = '2'
                ans[right - 2] = '%'
                right -= 2
            else:
                ans[right] = ans[left]
            right -= 1
            left -= 1
        return ''.join(ans)

s = "We are happy."
ss = Solution()
print(ss.replaceSpace(s))