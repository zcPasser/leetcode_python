from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        que = deque()
        que.extend([p, q])
        while que:
            left = que.popleft()
            right = que.popleft()
            if not left and not right:
                continue
            if not left or not right or (left.val != right.val):
                return False
            que.extend([left.left, right.left])
            que.extend([left.right, right.right])

        return True