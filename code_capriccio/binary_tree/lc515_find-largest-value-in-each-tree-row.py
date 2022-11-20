from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: [TreeNode]) -> list[int]:
        ans = []
        if root:
            que = deque()
            que.append(root)
            while que:
                max_of_level = que[0].val
                size = len(que)
                for _ in range(size):
                    p = que.popleft()
                    max_of_level = max(max_of_level, p.val)
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)
                ans.append(max_of_level)
        return ans