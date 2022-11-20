
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归函数：统计 以root为 根节点 子树 的左右子树 是否 平衡
    def isBalanced(self, root: TreeNode) -> bool:
        # 边界：空树。
        if root is None:
            return True

        # 递归函数：统计 以root为 根节点 的子树 的高度。
        def count_height_of_subtree(root):
            if root is None:
                return 0
            return 1 + max(count_height_of_subtree(root.left), count_height_of_subtree(root.right))
        # 获取 当前root子树 的 左右子树 高度
        left_height = count_height_of_subtree(root.left)
        right_height = count_height_of_subtree(root.right)

        return abs(left_height - right_height) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)