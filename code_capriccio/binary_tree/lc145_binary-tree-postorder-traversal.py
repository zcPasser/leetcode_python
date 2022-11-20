# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 统一迭代 实现
    def postorderTraversal(self, root: [TreeNode]) -> list[int]:
        ans = []
        stack_list = []
        if root:
            stack_list.append(root)
            while stack_list:
                p = stack_list.pop()
                if p:
                    stack_list.append(p)
                    stack_list.append(None)
                    if p.right:
                        stack_list.append(p.right)
                    if p.left:
                        stack_list.append(p.left)

                else:
                    p = stack_list.pop()
                    ans.append(p.val)
        return ans
    # 迭代 实现
    # def postorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     ans = []
    #     if root:
    #        stack_list = []
    #        stack_list.append(root)
    #        while stack_list:
    #             p = stack_list.pop()
    #             ans.append(p.val)
    #             # 先 将 左子树入栈，出栈 同时 处理节点 就在后。
    #             if p.left:
    #                 stack_list.append(p.left)
    #             if p.right:
    #                 stack_list.append(p.right)
    #     return ans[::-1]
    # 递归 实现
    # def postorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     ans = []
    #
    #     def traversal(r: TreeNode):
    #         if not r:
    #             return
    #         traversal(r.left)
    #         traversal(r.right)
    #         ans.append(r.val)
    #
    #     traversal(root)
    #     return ans