# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: [TreeNode]) -> list[int]:
        ans = []
        if root:
            que = deque()
            que.append(root)
            while que:
                size = len(que)
                ans.append(que[-1].val)
                for i in range(size):
                    p = que.popleft()
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)

        return ans