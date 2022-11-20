#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py100_TheSameTree.py
# @Time      :2022/2/14 22:26
# @Author    :zhangcai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 递归 实现
    # 深度优先遍历
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     # 先根序列 比较
    #     def pre_order(lchild: TreeNode, rchild: TreeNode):
    #         if lchild and rchild:
    #             if lchild.val == rchild.val:
    #                 return pre_order(lchild.left, rchild.left) \
    #                        and pre_order(lchild.right, rchild.right)
    #             else:
    #                 return False
    #         if not lchild and not rchild:
    #             return True
    #
    #         return False
    #     return pre_order(p, q)

    # 非递归 实现
    # 广度优先
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (not p and q):
            return False

        queue = []
        queue.append(p)
        queue.append(q)

        while queue:
            node_p = queue.pop(0)
            node_q = queue.pop(0)

            # 比较：结构、值
            if not node_p and not node_q:
                continue
            # 结构
            if (node_p and not node_q) or (not node_p and node_q):
                return False
            # 值
            if node_p.val != node_q.val:
                return False
            # 从广度上 入队
            queue.append(node_p.left)
            queue.append(node_q.left)
            queue.append(node_p.right)
            queue.append(node_q.right)
        return True

def main():
    return


if __name__ == "__main__":
    main()