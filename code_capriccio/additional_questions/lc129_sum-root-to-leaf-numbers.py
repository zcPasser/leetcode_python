# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def traversal(self, root: [TreeNode], path: list, cur_val: int):
        # 处理 中
        cur_val = (cur_val * 10) + root.val
        if not root.left and not root.right:
            self.ans += cur_val
            return
        # 处理 左——非空节点
        if root.left:
            # 入栈，记录轨迹
            path.append(root.left)
            # 递归
            self.traversal(root.left, path, cur_val)
            # 回溯
            path.pop()
        if root.right:
            path.append(root.right)
            self.traversal(root.right, path, cur_val)
            path.pop()
        return

    def sumNumbers(self, root: [TreeNode]) -> int:
        if not root:
            return self.ans
        path = [root]
        self.traversal(root, path, 0)
        return self.ans
