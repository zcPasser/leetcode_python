# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traversal(self, root1: TreeNode, root2: TreeNode):
        if not root1 and not root2:
            return True
        elif (not root1 and root2) or (not root2 and root1):
            return False
        elif root1.val != root2.val:
            return False
        left = self.traversal(root1.left, root2.left)
        right = self.traversal(root1.right, root2.right)

        return left and right

    def isSameTree(self, p: [TreeNode], q: [TreeNode]) -> bool:
        return self.traversal(p, q)
