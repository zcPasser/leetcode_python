from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: [TreeNode]) -> int:
        ans = 0
        if root:
            que = deque()
            que.append(root)
            while que:
                size = len(que)
                ans += 1
                for _ in range(size):
                    p = que.popleft()
                    if not p.left and not p.right:
                        return ans
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)
        return ans