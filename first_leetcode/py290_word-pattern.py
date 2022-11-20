"""
1、描述
给定一种规律 pattern和一个字符串s，判断 s是否遵循相同的规律。

这里的遵循指完全匹配，例如，pattern里的每个字母和字符串s中的每个非空单词之间存在着双向连接的对应规律。

2、提示
. 1 <= pattern.length <= 300
. pattern只包含小写英文字母
. 1 <= s.length <= 3000
. s只包含小写英文字母和' '
. s不包含 任何前导或尾随对空格
. s中每个单词都被 单个空格 分隔
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # words = s.split()
        # len_words = len(words)
        # if len(pattern) != len_words:
        #     return False
        # words_to_pattern_map, pattern_to_words_map = dict(), dict()
        # for i in range(len_words):
        #     if pattern[i] in pattern_to_words_map and pattern_to_words_map[pattern[i]] != words[i]:
        #         return False
        #     else:
        #         pattern_to_words_map[pattern[i]] = words[i]
        #     if words[i] in words_to_pattern_map and words_to_pattern_map[words[i]] != pattern[i]:
        #         return False
        #     else:
        #         words_to_pattern_map[words[i]] = pattern[i]
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False

        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word

        return True
