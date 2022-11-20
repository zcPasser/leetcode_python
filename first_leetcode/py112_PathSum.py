# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 采用 先序遍历 非递归形式。
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # 边界：1-空树；
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and path == targetSum:
                return True
            if node.left:
                stack.append((node.left, path + node.left.val))
            if node.right:
                stack.append((node.right, path + node.right.val))
        return False

    # 采用 先序遍历 递归形式。
    # def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    #     def preOrder(root: TreeNode, current_sum: int):
    #         if root is not None:
    #             # 获取 当前节点 的值。
    #             current_sum += root.val
    #             # 当前 叶子节点。
    #             if root.left is None and root.right is None and current_sum == targetSum:
    #                 return True
    #             return preOrder(root.left, current_sum) or preOrder(root.right, current_sum)
    #         else:
    #             # 空树 返回false。
    #             return False
    #
    #     return preOrder(root, 0)



