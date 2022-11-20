class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack_list = []
        # 删除 重复元素
        for ch in s:
            if stack_list and stack_list[-1] == ch:
                stack_list.pop()
            else:
                stack_list.append(ch)
        # 打印 新字符串
        return ''.join(stack_list)