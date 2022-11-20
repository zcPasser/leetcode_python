"""
1、一个排序后的字符列表 letters ，列表中只包含小写英文字母。
2、一个目标字母 target。
3、寻找在这一有序列表里比目标字母大的最小字母。若是未找到，则返回letters中最小字符。

返回：
   有序列表里比目标字母大的最小字母。
"""


class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]

        left, right = 0, len(letters) - 1

        while left < right:
            mid = left + (right - left) // 2
            if target < letters[mid]:
                right = mid
            else:
                left = mid + 1

        return letters[left]
        # ord_target = ord(target)
        # for s in letters:
        #     if ord_target < ord(s):
        #         return s
        # return letters[0]

