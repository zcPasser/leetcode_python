class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: [TreeNode]) -> int:
        pre = None
        ans = 100001
        def helper(node: TreeNode):
            if not node:
                return
            if node.left:
                helper(node.left)
            nonlocal pre
            nonlocal ans
            if pre:
                ans = min(ans, abs(node.val - pre.val))
                if ans == 1:
                    return
            pre = node
            if node.right:
                helper(node.right)

        helper(root)
        return ans