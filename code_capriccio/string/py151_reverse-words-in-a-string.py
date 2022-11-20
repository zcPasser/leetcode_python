import re


class Solution:
    def reverseWords(self, s: str) -> str:
        fast, slow = 0, 0
        s_list = list(s)
        len_s = len(s)
        # 双指针 去除 空格
        while fast < len_s:
            # 对 非目标元素（非空格） 操作
            if s_list[fast] != ' ':
                # 手动控制， 保证 除了第一个 单词，其他单词前 有 一个 空格。
                if slow != 0:
                    s_list[slow] = ' '
                    slow += 1
                # 处理好当前 单词前 的 空格问题，处理 当前单词。
                while fast < len_s and s_list[fast] != ' ':
                    s_list[slow] = s_list[fast]
                    slow += 1
                    fast += 1
            fast += 1

        # 反转pattern,[start, end]闭区间。
        def reverse(pattern: list, start: int, end: int):
            while start < end:
                pattern[start], pattern[end] = pattern[end], pattern[start]
                start += 1
                end -= 1

        # 整体 反转
        reverse(s_list, 0, slow - 1)
        # 开始 对 每个 单词反转，恢复正常词序。
        i, j = 0, 0
        while j < slow:
            if s_list[j] == ' ':
                reverse(s_list, i, j - 1)
                i = j + 1
            j += 1
        # 对 末尾 单词 反转
        reverse(s_list, i, slow - 1)

        return ''.join(s_list[:slow])


    # def reverseWords(self, s: str) -> str:
    #     pattern = re.compile(r'\d|[a-z|A-Z]+')
    #     words = pattern.findall(s)
    #     # print(words)
    #     return ' '.join(words[::-1])


s = "  hello world  "
ss = Solution()
print(ss.reverseWords(s))