#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py35_SearchForInsertionPosition.py
# @Time      :2022/2/19 21:03
# @Author    :zhangcai

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1

        nums.insert(low, target)
        return low

def main():
    return


if __name__ == "__main__":
    main()