# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: [TreeNode]) -> [TreeNode]:
        pre = 0
        def helper(node: TreeNode):
            if not node:
                return
            helper(node.right)
            nonlocal pre
            node.val += pre
            pre = node.val
            helper(node.left)

            return node
        helper(root)
        return root