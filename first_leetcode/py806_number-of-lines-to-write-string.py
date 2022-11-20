

class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        cnt_of_lines, width_of_cur_line = 1, 0
        datum = ord('a')
        for ch in s:
            width_of_ch = widths[ord(ch) - datum]
            width_of_cur_line += width_of_ch
            if width_of_cur_line > 100:
                width_of_cur_line = width_of_ch
                cnt_of_lines += 1

        return [cnt_of_lines, width_of_cur_line]


width = [3,4,10,4,8,7,3,3,4,9,8,2,9,6,2,8,4,9,9,10,2,4,9,10,8,2]
s = "mqblbtpvicqhbrejb"
so = Solution()
print(so.numberOfLines(width, s))