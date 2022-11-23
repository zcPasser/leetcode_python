from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代实现
    def isSymmetric(self, root: [TreeNode]) -> bool:
        if root:
            que = deque()
            que.extend([root.left, root.right])
            while que:
                left = que.popleft()
                right = que.popleft()
                # 处理 含空节点的情形。
                if not left and not right:
                    continue
                elif left and not right:
                    return False
                elif not left and right:
                    return False
                # 处理 不含空节点的情形：对应左右节点值不相等，从而不可翻转。
                elif left.val != right.val:
                    return False
                # 外侧
                que.extend([left.left, right.right])
                # 内侧
                que.extend([left.right, right.left])

        return True
    # 递归实现
    # def isSymmetric(self, root: [TreeNode]) -> bool:
    #     # 比较 当前根节点 左右子树中的各自对应节点 是否可翻转。
    #     def compare(left: TreeNode, right: TreeNode) -> bool:
    #         # 处理 含空节点的情形。
    #         if not left and not right:
    #             return True
    #         elif left and not right:
    #             return False
    #         elif not left and right:
    #             return False
    #         # 处理 不含空节点的情形：对应左右节点值不相等，从而不可翻转。
    #         elif left and right and left.val != right.val:
    #             return False
    #         # 比较当前 对应的 左右节点的 外侧 和 内侧 是否 能够 各自翻转。
    #         outside = compare(left.left, right.right)
    #         inside = compare(left.right, right.left)
    #
    #         return outside and inside
    #     if root:
    #         return compare(root.left, root.right)
    #     return True