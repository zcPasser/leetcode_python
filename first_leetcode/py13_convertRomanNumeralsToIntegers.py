#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py13_convertRomanNumeralsToIntegers.py
# @Time      :2022/2/13 19:38
# @Author    :zhangcai

# 13. 罗马数字转整数
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
class Solution:
    def romanToInt(self, s: str) -> int:
        hashtable1 = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        hashtable2 = {'IV' : 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        len_s = len(s)
        res = 0
        i = 0
        # mid = len_s // 2
        while i < len_s:
            if i < len_s - 1 and hashtable1[s[i]] < hashtable1[s[i + 1]]:
                res += hashtable2[s[i : i+2]]
                i += 2
            else:
                res += hashtable1[s[i]]
                i += 1
        return res

# 若存在小的数字在大的数字的左边的情况，根据规则需要减去小的数字。
# 对于这种情况，我们也可以将每个字符视作一个单独的值，若一个数字右侧的数字比它大，则将该数字的符号取反。
#
# 例如 XIV 可视作 \texttt{X}-\texttt{I}+\texttt{V}=10-1+5=14X−I+V=10−1+5=14。
    SYMBOL_VALUES = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    def romanToInt2(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i, ch in enumerate(s):
            value = Solution.SYMBOL_VALUES[ch]
            if i < n - 1 and value < Solution.SYMBOL_VALUES[s[i + 1]]:
                ans -= value
            else:
                ans += value
        return ans

def main():
    test = Solution()
    s = 'MCMXCIV'
    print('res = {0}'.format(test.romanToInt(s)))
    return


if __name__ == "__main__":
    main()