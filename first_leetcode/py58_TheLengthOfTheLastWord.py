#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py58_TheLengthOfTheLastWord.py
# @Time      :2022/2/20 11:18
# @Author    :zhangcai

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        return len(s.strip().split(' ')[-1])

def main():
    return


if __name__ == "__main__":
    main()