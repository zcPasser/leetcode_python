# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: [TreeNode]) -> int:
        if not root:
            return 0
        ans = self.rob_tree(root)
        return max(ans[0], ans[1])

    def rob_tree(self, cur: [TreeNode]) -> list[int]:
        if not cur:
            return [0, 0]
        left = self.rob_tree(cur.left)
        right = self.rob_tree(cur.right)
        # 偷
        val1 = cur.val + left[0] + right[0]
        # 不偷
        val2 = max(left[0], left[1]) + max(right[0], right[1])

        return [val2, val1]
