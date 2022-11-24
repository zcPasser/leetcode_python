from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归实现——后序遍历，结合 完全二叉树特点。
    def countNodes(self, root: [TreeNode]) -> int:
        def helper(node: TreeNode) -> int:
            if not node:
                return 0
            left, right = node.left, node.right
            left_depth, right_depth =0, 0
            while left:
                left_depth += 1
                left = left.left
            while right:
                right_depth += 1
                right = right.right
            if left_depth == right_depth:
                return (2 << left_depth) - 1
            left_cnts = helper(node.left)
            right_cnts = helper(node.right)

            cnts = 1 + left_cnts + right_cnts
            return cnts
        return helper(root)
    # 递归实现——后序遍历，类似求高度的模板
    # def countNodes(self, root: [TreeNode]) -> int:
    #     def helper(node: TreeNode) -> int:
    #         if not node:
    #             return 0
    #         left_cnts = helper(node.left)
    #         right_cnts = helper(node.right)
    #
    #         cnts = 1 + left_cnts + right_cnts
    #         return cnts
    #     return helper(root)
    # 迭代实现——层序遍历
    # def countNodes(self, root: [TreeNode]) -> int:
    #     ans = 0
    #     if root:
    #         que = deque()
    #         que.append(root)
    #         # depth = 0
    #         while que:
    #             size = len(que)
    #             ans += size
    #             for _ in range(size):
    #                 p = que.popleft()
    #                 if p.left:
    #                     que.append(p.left)
    #                 if p.right:
    #                     que.append(p.right)
    #
    #     return ans