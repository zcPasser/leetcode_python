"""
给定两个字符串 s 和 t ，判断它们是否是同构的。

如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

"""


class Solution:
    # 双射：每个y都有x对应，而且都是一一对应。
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 先判断 长度 是否合法。
        s_len = len(s)

        x_dict = {}
        y_dict = {}

        for i in range(s_len):
            x, y = s[i], t[i]
            x_y, y_x = x_dict.get(x, '-1'), y_dict.get(y, '-1')
            # 未建立 x<->y 映射关系，添加映射关系。
            if x_y == '-1' and y_x == '-1':
                x_dict[x] = y
                y_dict[y] = x
            # 映射关系 未遵守 双射 原则。
            elif x_y != y or y_x != x:
                return False

        return True


s1 = "badc"
t1 = "baba"
ss = Solution()
ss.isIsomorphic(s1, t1)
