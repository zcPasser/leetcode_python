

class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        len_of_s = len(s)
        max_num, min_num = len_of_s, 0
        ans = []
        for ch in s:
            if ch == 'I':
                ans.append(min_num)
                min_num += 1
            else:
                ans.append(max_num)
                max_num -= 1
        ans.append(max_num)
        return ans


so = Solution()
s = "DDI"
print(so.diStringMatch(s))