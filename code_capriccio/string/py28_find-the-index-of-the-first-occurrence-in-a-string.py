class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 前缀表 不减一、不右移 版本。

        # 获取 next数组。
        def get_next(pattern: str) -> list:
            # next数组 初始化
            len_pattern = len(pattern)
            next_list = [0] * len_pattern
            # 当前 字符串 是 [0, i] 区间 的 子串
            # 指针 j 表示：当前 字符串 的 前缀末尾 位置，
            # 同时 j 也表示：当前字符串 及其 之前所有子串 的 最长相同前后缀 长度。
            j = 0
            # 指针 i 表示：后缀 末尾位置。
            for i in range(1, len_pattern):
                # 处理 前后缀 不相同。
                while j > 0 and pattern[j] != pattern[i]:
                    j = next_list[j - 1]
                # 处理 前后缀 相同
                if pattern[i] == pattern[j]:
                    j += 1
                # 更新 next数组
                next_list[i] = j
            return next_list

        next_list = get_next(pattern=needle)
        j = 0
        len_needle = len(needle)
        for i in range(len(haystack)):
            # 处理 比较过程中 冲突情形，模式串的 指针 不断 后退，直至0.
            while j > 0 and haystack[i] != needle[j]:
                j = next_list[j - 1]
            # 文本串 与 模式串 当前位置成功匹配。
            if needle[j] == haystack[i]:
                j += 1
            # 匹配成功，即 模式串 指针 越界。
            if j == len_needle:
                # 文本串 中 匹配成功 位置如下;
                return i - len_needle + 1
        return -1