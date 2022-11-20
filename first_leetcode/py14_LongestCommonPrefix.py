#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py14_LongestCommonPrefix.py
# @Time      :2022/2/16 14:29
# @Author    :zhangcai

class Solution:
    def longestCommonPrefix(self, strs):
        if strs is None or strs == [] or '' in strs:
            return ''
        if len(strs) == 1:
            return strs[0]

        s1 = min(strs)
        s2 = max(strs)
        print('s1=', s1, 's2=', s2)

        for i,x in enumerate(s1):
            if x != s2[i]:
                return s1[:i]
        return s1


def main():
    s = ['flower', 'flow', 'flight', ]
    solution = Solution()
    print(solution.longestCommonPrefix(s))

    #
    return


if __name__ == "__main__":
    main()