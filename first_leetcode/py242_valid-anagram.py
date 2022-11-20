"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若s 和 t中每个字符出现的次数都相同，则称s 和 t互为字母异位词。

提示:
1、1 <= s.length, t.length <= 5 * 104
2、s 和 t仅包含小写字母

进阶:如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

思路：
法一：按照 定义 表层含义，统计字符串中各字符的次数，再比较。
法二：字母异位词 的2个字符串 按照 字典排序后，完全相同。

"""


class Solution:
    # 法一：字典 统计次数。
    # def isAnagram(self, s: str, t: str) -> bool:
    #     if len(s) != len(t):
    #         return False
    #
    #     def count_char(ss):
    #         count = dict()
    #         for ch in ss:
    #             count[ch] = 1 if ch not in count else count[ch] + 1
    #
    #         return count
    #
    #     count_s, count_t = count_char(s), count_char(t)
    #     # 比较 2个 字典。
    #     for k, v in count_s.items():
    #         # 相异 条件：1、字符不存在。  2、字符次数不一致。
    #         if k not in count_t or count_t[k] != v:
    #             return False
    #     return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s, t = sorted(s), sorted(t)
        for c1, c2 in zip(s, t):
            if c1 != c2:
                return False
        return True

s, t = 'rat', 'car'
solution = Solution()
print(solution.isAnagram(s, t))
