
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        s_list = list(s)
        len_s = len(s)
        # 反转pattern,[start, end]闭区间。
        def reverse(pattern: list, start: int, end: int):
            while start < end:
                pattern[start], pattern[end] = pattern[end], pattern[start]
                start += 1
                end -= 1
        reverse(s_list, 0, n - 1)
        reverse(s_list, n, len_s - 1)
        return ''.join(s_list[::-1])


s = "abcdefg"
n = 2
ss = Solution()
print(ss.reverseLeftWords(s, n))

