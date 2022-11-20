from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: [TreeNode]) -> list[float]:
        ans = []
        if root:
            que = deque()
            que.append(root)
            while que:
                sum_of_cur_sum = 0
                size = len(que)
                for _ in range(size):
                    p = que.popleft()
                    sum_of_cur_sum += p.val
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)
                ans.append(sum_of_cur_sum / size)
        return ans