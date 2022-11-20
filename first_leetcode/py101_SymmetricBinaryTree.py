#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py101_SymmetricBinaryTree.py
# @Time      :2022/2/21 10:30
# @Author    :zhangcai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 深度DFS-递归
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p: TreeNode,q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)
        if not root:
            return True
        return check(root.left, root.right)

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     # 队列， 用于存储 BFS 序列
    #     queue = []
    #     # p ：遍历 二叉树的指针
    #     p = root
    #     queue.append(p)
    #
    #     while len(queue) > 0:
    #         # 对当前序列轴对称 判断
    #         if not self.sequence_symmetry(queue):
    #             return False
    #         # 记录 一层操作的 出队 次数
    #         len_queue = len(queue)
    #         # 更新存储 下一层
    #         for i in range(len_queue):
    #             p = queue.pop(0)
    #             if p is None:
    #                 continue
    #             # 存储 p 的孩子
    #             queue.append(p.left)
    #             queue.append(p.right)
    #
    #     return True

    # 判断 线性序列 轴对称
    # 即 二叉树 的 同一层结点 的 轴对称
    # 注意：空结点 也要特殊存储
    def sequence_symmetry(self, sequences: list) -> bool:
        len_sequences = len(sequences)
        k = len_sequences // 2

        for i in range(k):
            if not sequences[i] and not sequences[len_sequences - 1 - i]:
                continue
            if (not sequences[i] and sequences[len_sequences - 1 - i]) \
                or (sequences[i] and not sequences[len_sequences - 1 - i]) \
                or (sequences[i].val != sequences[len_sequences - 1 - i].val):

                return False

        return True

def main():
    root = TreeNode(1)
    p = root
    # [1, 2, 2, 3, 4, 4, 3]
    p.left = TreeNode(2)
    p.right = TreeNode(2)
    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)
    p.right.left = TreeNode(4)
    p.right.right = TreeNode(3)

    s = Solution()
    print(s.isSymmetric(root))

    return


if __name__ == "__main__":
    main()