#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py20_ValidParentheses.py
# @Time      :2022/2/16 16:01
# @Author    :zhangcai

class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        query_dict = {
                   '(' : ')',
                    '{' : '}',
                    '[' : ']'
                }
        for i in s:
            if i in query_dict.keys():
                stack_list.append(i)
            elif len(stack_list) == 0 or query_dict[stack_list.pop()] != i:
                return False
        return len(stack_list) == 0

def main():
    s = "]"
    ss = Solution()
    print(ss.isValid(s))
    return


if __name__ == "__main__":
    main()