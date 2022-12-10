# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归实现
    def trimBST(self, root: [TreeNode], low: int, high: int) -> [TreeNode]:
        def helper(node: TreeNode, l: int, h: int) -> [TreeNode]:
            if not node:
                return None
            # 处理 中节点
            if node.val < l:
                return helper(node.right, l, h)
            if node.val > h:
                return helper(node.left, l, h)
            # 处理 左
            node.left = helper(node.left, l, h)
            # 处理 右
            node.right = helper(node.right, l, h)

            return node
        return helper(root, low, high)

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)
left, right = 1, 2
s = Solution()
print(s.trimBST(root, left, right))