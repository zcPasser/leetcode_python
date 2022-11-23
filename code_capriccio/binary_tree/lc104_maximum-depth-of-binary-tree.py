from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: [TreeNode]) -> int:
        def get_height(node: TreeNode) -> int:
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            node_height = 1 + max(left_height, right_height)
            return node_height
        ans = 0
        if root:
            que = deque()
            que.append(root)
            while que:
                size = len(que)
                ans += 1
                for _ in range(size):
                    p = que.popleft()
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)
        return ans