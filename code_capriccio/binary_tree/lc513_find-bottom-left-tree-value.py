from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归实现——后序遍历
    def findBottomLeftValue(self, root: [TreeNode]) -> int:
        max_depth = 0
        ans = 0
        def helper(node: TreeNode, depth: int) -> None:
            nonlocal max_depth
            nonlocal ans
            if not node.left and not node.right:
                if depth > max_depth:
                    max_depth = depth
                    ans = node.val
                    return
            if node.left:
                helper(node.left, depth + 1)
            if node.right:
                helper(node.right, depth + 1)
        if root:
            helper(root, 1)
        return ans
    # 迭代实现——层序遍历
    def findBottomLeftValue(self, root: [TreeNode]) -> int:
        ans = 0
        if root:
            que = deque()
            que.append(root)
            while que:
                size = len(que)
                ans = que[0].val
                for _ in range(size):
                    p = que.popleft()
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)

        return ans