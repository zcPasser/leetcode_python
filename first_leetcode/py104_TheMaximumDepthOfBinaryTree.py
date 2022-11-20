#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :py104_TheMaximumDepthOfBinaryTree.py
# @Time      :2022-02-24 19:53
# @Author    :zhangcai

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS 递归实现
    # def maxDepth(self, root: [TreeNode]) -> int:
    #     if not root:
    #         return 0
    #     left_depth = self.maxDepth(root.left) + 1
    #     right_depth = self.maxDepth(root.right) + 1
    #
    #     return left_depth if left_depth > right_depth else right_depth

    # BFS 队列实现
    def maxDepth(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        queue = []
        queue.append(root)
        ans = 1

        while len(queue) > 0:
            len_queue = len(queue)
            for i in range(len_queue):
                p = queue.pop(0)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            ans += 1


        return ans

def main():
    return


if __name__ == "__main__":
    main()