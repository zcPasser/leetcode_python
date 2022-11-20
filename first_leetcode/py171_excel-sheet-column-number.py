"""
给你一个字符串 columnTitle ，表示 Excel 表格中的列名称。返回 该列名称对应的列序号 。

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

"""


class Solution:
    # 核心：26进制转换。
    # 当前位数值、进位。
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for ch in columnTitle:
            num = ord(ch) - ord('A') + 1
            res = res * 26 + num

        return res
