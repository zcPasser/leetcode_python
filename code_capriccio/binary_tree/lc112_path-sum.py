# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代实现
    def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
        if root:
            stack = []
            stack.append((root, targetSum - root.val))
            while stack:
                (p, cnt) = stack.pop()
                if p:
                    if p.right:
                        stack.append((p.right, cnt - p.right.val))
                    if p.left:
                        stack.append((p.left, cnt - p.left.val))
                    stack.append((p, cnt))
                    stack.append((None, 0))
                else:
                    (p, cnt) = stack.pop()
                    if not p.left and not p.right:
                        if cnt == 0:
                            return True

        return False
    # 递归实现
    # def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
    #     def helper(node: TreeNode, cnt: int) -> bool:
    #         # 三部曲——终止条件：叶子节点
    #         if not node.left and not node.right:
    #             if cnt == 0:
    #                 return True
    #             else:
    #                 return False
    #         # 三部曲——单层逻辑：前序遍历之中前后
    #         # 处理 左（过滤 空节点）
    #         if node.left:
    #             # 递归 左
    #             # cnt - node.left.val 传参形式 回溯
    #             if helper(node.left, cnt - node.left.val):
    #                 return True
    #         if node.right:
    #             if helper(node.right, cnt - node.right.val):
    #                 return True
    #         return False
    #     if root:
    #         return helper(root, targetSum - root.val)
    #     return False
    # def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
    #     def helper(node: TreeNode, cur_sum: int) -> bool:
    #         # 三部曲——终止条件：叶子节点
    #         if not node.left and not node.right:
    #             if node.val + cur_sum == targetSum:
    #                 return True
    #             else:
    #                 return False
    #         ans = False
    #         # 三部曲——单层逻辑：前序遍历之中前后
    #         if node.left:
    #             ans = helper(node.left, cur_sum + node.val)
    #         if not ans and node.right:
    #             ans = helper(node.right, cur_sum + node.val)
    #
    #         return ans
    #     ans = False
    #     if root:
    #         ans = helper(root, 0)
    #     return ans