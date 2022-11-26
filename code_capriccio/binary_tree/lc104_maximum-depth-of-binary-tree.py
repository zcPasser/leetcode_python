from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归实现-前序遍历
    def maxDepth(self, root: [TreeNode]) -> int:
        ans = 0
        def helper(node: TreeNode, depth: int):
            # 终止条件，但在 进入递归前以处理。
            # if not node:
            #     return
            # 该关键字方便使用外层函数的 变量
            nonlocal ans
            # 处理 中
            ans = max(ans, depth)
            # 处理 左
            # 进入 递归前处理，相当于三部曲中的终止条件
            if node.left:
                # 进入 左子树前，将其深度更新+1
                depth += 1
                helper(node.left, depth)
                # 结束 左子树遍历，返回后，将深度值 回溯-1
                depth -= 1
            # 处理 右
            if node.right:
                depth += 1
                helper(node.right, depth)
                depth -= 1
            return
        # 递归三部曲中的终止条件
        if root:
            helper(root, 1)
        return ans


    # def maxDepth(self, root: [TreeNode]) -> int:
    #     def get_height(node: TreeNode) -> int:
    #         if not node:
    #             return 0
    #         left_height = get_height(node.left)
    #         right_height = get_height(node.right)
    #         node_height = 1 + max(left_height, right_height)
    #         return node_height
    #     ans = 0
    #     if root:
    #         que = deque()
    #         que.append(root)
    #         while que:
    #             size = len(que)
    #             ans += 1
    #             for _ in range(size):
    #                 p = que.popleft()
    #                 if p.left:
    #                     que.append(p.left)
    #                 if p.right:
    #                     que.append(p.right)
    #     return ans