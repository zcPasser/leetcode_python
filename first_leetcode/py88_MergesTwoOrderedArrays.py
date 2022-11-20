#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py88_MergesTwoOrderedArrays.py
# @Time      :2022/2/20 19:22
# @Author    :zhangcai

class Solution:
    # def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     last = 0
    #     for i in range(n):
    #         flag = False
    #         for j in  range(last, m + i + 1):
    #             if nums1[j] > nums2[i]:
    #                 nums1.insert(j, nums2[i])
    #                 last += 1
    #                 nums1.pop()
    #                 flag = True
    #                 break
    #         # nums1 末尾插入 ，即对 ‘0’ 元素 覆盖
    #         if not flag:
    #             nums1[m + i] = nums2[i]
    #             last += 1
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 逆序双指针
        i = m - 1
        j = n - 1
        len_ = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[len_] = nums2[j]
                j -= 1
            else:
                nums1[len_] = nums1[i]
                i -= 1
            len_ -= 1

        while j >= 0:
            nums1[len_] = nums2[j]
            j -= 1
            len_ -= 1



def main():
    s = Solution()
    nums1, nums2 = [1,2,3,0,0,0], [2,5,6]
    print(nums1)
    m, n = 3, 3
    s.merge(nums1, m, nums2, n)
    print(nums1)
    return


if __name__ == "__main__":
    main()