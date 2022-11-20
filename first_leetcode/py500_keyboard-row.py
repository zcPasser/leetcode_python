"""
给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

第一行由字符 "qwertyuiop" 组成。
第二行由字符 "asdfghjkl" 组成。
第三行由字符 "zxcvbnm" 组成。

"""
class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        res = []
        char_dict = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1,
                     'a': 2, 's': 2, 'd': 2, 'f': 2, 'g': 2, 'h': 2, 'j': 2, 'k': 2, 'l': 2,
                     'z': 3, 'x': 3, 'c': 3, 'v': 3, 'b': 3, 'n': 3, 'm': 3}
        for s in words:
            ss = s.lower()
            line_number = char_dict[ss[0]]
            for ch in ss:
                if char_dict[ch] != line_number:
                    line_number = char_dict[ch]
                    break
            if line_number == char_dict[ss[0]]:
                res.append(s)

        return res
