#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py94_MiddleOrderTraversalOfBinaryTrees.py
# @Time      :2022/2/20 21:56
# @Author    :zhangcai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 非递归 实现
    def inorderTraversal(self, root: [TreeNode]) -> list[int]:
        res = []
        stack = []
        p = root
        while p or len(stack) > 0:
            if p:
                stack.append(p)
                p = p.left
            else:
                # 栈顶结点 没有左孩子
                p = stack.pop()
                # 访问 根结点
                res.append(p.val)
                # 进入 当前根结点 的 右子树
                p = p.right
        return res


    # 递归 实现
    # def inorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     res = []
    #     self.inOrder(root, res)
    #     return res
    #
    # def inOrder(self, root: [TreeNode], res: list[int]):
    #     if root:
    #         self.inOrder(root.left, res)
    #         res.append(root.val)
    #         self.inOrder(root.right, res)

def main():
    return


if __name__ == "__main__":
    main()