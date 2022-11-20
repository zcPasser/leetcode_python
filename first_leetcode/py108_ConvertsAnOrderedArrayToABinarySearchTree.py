#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py108_ConvertsAnOrderedArrayToABinarySearchTree.py
# @Time      :2022-02-25 10:22
# @Author    :zhangcai

'''
    leetcode：108-将有序数组转换为二叉搜索树
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        nums_len = len(nums)
        # 边界：1-空树；2-只有根结点。
        if nums_len == 0:
            return None
        if nums_len == 1:
            return TreeNode(val=nums[0])

        start, end = 0, nums_len - 1

        def BST(nums, start, end):
            # 边界：1-非法即空树；2-只有根节点。
            if start > end or start < 0 or end < 0:
                return None
            if start == end:
                return TreeNode(val=nums[start])

            mid = (start + end) // 2
            root = TreeNode(val=nums[mid])
            root.left = BST(nums, start, mid - 1)
            root.right = BST(nums, mid + 1, end)
            return root

        return BST(nums, start, end)


def main():
    return


if __name__ == "__main__":
    main()