# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        def recursion_invert(r: TreeNode):
            if r:
                temp_node = r.left
                r.left, r.right = r.right, temp_node
                recursion_invert(r.left)
                recursion_invert(r.right)
        recursion_invert(root)
        return root
