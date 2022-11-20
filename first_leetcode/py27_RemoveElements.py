#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py27_RemoveElements.py
# @Time      :2022/2/17 18:47
# @Author    :zhangcai

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if not nums:
            return 0
        len_nums = len(nums)
        start, end = 0, len_nums - 1

        if start == end and nums[start] == val:
            nums.clear()
            return 0

        while start <= end:
            if nums[start] == val:
                if nums[end] != val:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                end -= 1
            else:
                start += 1

        return start + 1 if start == end else start




def main():
    s = Solution()
    nums = [4, 4]
    print(s.removeElement(nums, 4))
    return


if __name__ == "__main__":
    main()