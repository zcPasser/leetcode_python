# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 迭代实现
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
    # 递归实现
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(node: TreeNode, pp: TreeNode, qq: TreeNode) -> [TreeNode]:
            if not node:
                return None
            if node.val < pp.val and node.val < qq.val:
                return helper(node.right, pp, qq)

            if node.val > pp.val and node.val > qq.val:
                return helper(node.left, pp, qq)

            return node
        return helper(root, p, q)