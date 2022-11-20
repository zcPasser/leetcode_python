#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py26_RemovesDuplicatesFromAnOrderedArray.py
# @Time      :2022/2/16 17:26
# @Author    :zhangcai

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        slow, fast = 0, 1
        len_nums = len(nums)
        while fast < len_nums:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1


def main():
    return


if __name__ == "__main__":
    main()