from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归实现——后序遍历
    def minDepth(self, root: [TreeNode]) -> int:
        def helper(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = helper(node.left)
            right_height = helper(node.right)
            if not node.left and node.right:
                return 1 + right_height
            if node.left and not node.right:
                return 1 + left_height
            return 1 + min(left_height, right_height)
        return helper(root)
    # 迭代实现——层序遍历
    # def minDepth(self, root: [TreeNode]) -> int:
    #     ans = 0
    #     if root:
    #         que = deque()
    #         que.append(root)
    #         while que:
    #             size = len(que)
    #             ans += 1
    #             for _ in range(size):
    #                 p = que.popleft()
    #                 if not p.left and not p.right:
    #                     return ans
    #                 if p.left:
    #                     que.append(p.left)
    #                 if p.right:
    #                     que.append(p.right)
    #     return ans