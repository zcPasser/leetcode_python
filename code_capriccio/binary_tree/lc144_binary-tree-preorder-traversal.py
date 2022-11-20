# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 统一迭代 实现
    def preorderTraversal(self, root: [TreeNode]) -> list[int]:
        ans = []
        stack_list = []
        if root:
            stack_list.append(root)
            while stack_list:
                p = stack_list.pop()
                if p:
                    if p.right:
                        stack_list.append(p.right)
                    if p.left:
                        stack_list.append(p.left)
                    stack_list.append(p)
                    stack_list.append(None)
                else:
                    p = stack_list.pop()
                    ans.append(p.val)
        return ans
    # 迭代 实现
    # def preorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     ans = []
    #     if root:
    #         stack_list = []
    #         stack_list.append(root)
    #         while stack_list:
    #             p = stack_list.pop()
    #             ans.append(p.val)
    #             if p.right:
    #                 stack_list.append(p.right)
    #             if p.left:
    #                 stack_list.append(p.left)
    #     return ans
    # 递归 实现
    # def preorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     ans = []
    #     def traversal(r: [TreeNode]):
    #         if not r:
    #             return
    #         ans.append(r.val)
    #         traversal(r.left)
    #         traversal(r.right)
    #
    #     traversal(root)
    #     return ans
