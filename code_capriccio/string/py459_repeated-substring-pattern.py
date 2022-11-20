
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def get_next(pattern: str) -> list[int]:
            # 初始化
            len_pattern = len(pattern)
            next_list = [0] * len_pattern
            # 指针 j 表示：当前 字符串 的 前缀末尾 位置，
            # 同时 j 也表示：当前字符串 及其 之前所有子串 的 最长相同前后缀 长度。
            j = 0
            # 当前 字符串 是 [0, i] 区间 的 子串
            # 指针 i 表示：后缀 末尾位置。
            for i in range(1, len_pattern):
                # 处理 前后缀 不相同
                while j > 0 and pattern[i] != pattern[j]:
                    j = next_list[j - 1]
                # 处理 前后缀 相同
                if pattern[i] == pattern[j]:
                    j += 1
                # 更新 next 数组
                next_list[i] = j
            return next_list
        next_list = get_next(s)
        len_s = len(s)
        # 判断条件：1、存在 相同公共前后缀。    2、字符串总长度 是 子串的倍数。
        if next_list[len_s - 1] != 0 and (len_s % (len_s - next_list[len_s - 1]) == 0):
            return True
        return False