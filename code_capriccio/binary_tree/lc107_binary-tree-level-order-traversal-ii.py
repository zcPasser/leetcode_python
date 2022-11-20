# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: [TreeNode]) -> list[list[int]]:
        ans = []
        if root:
            from collections import deque
            que = deque()
            que.append(root)
            while que:
                level_size = len(que)
                cur_level = []
                for _ in range(level_size):
                    p = que.popleft()
                    cur_level.append(p.val)
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)
                ans.append(cur_level)
        return ans[::-1]
