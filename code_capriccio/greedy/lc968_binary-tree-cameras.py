# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def traversal(self, node: [TreeNode]) -> int:
        if not node:
            return 2
        left = self.traversal(node.left)
        right = self.traversal(node.right)
        # 左右节点 都有 覆盖，则当前节点 相当于 叶子节点
        if left == 2 and right == 2:
            return 0
        if left == 0 or right == 0:
            self.ans += 1
            return 1
        if left == 1 or right == 1:
            return 2
        return -1

    def minCameraCover(self, root: [TreeNode]) -> int:
        root_val = self.traversal(root)
        if root_val == 0:
            self.ans += 1
        return self.ans
