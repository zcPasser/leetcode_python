# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归实现
    def getMinimumDifference(self, root: [TreeNode]) -> int:
        pre = None
        ans = 100001
        stack = [root]
        while stack:
            p = stack.pop()
            if p:
                if p.right:
                    stack.append(p.right)
                stack.append(p)
                stack.append(None)
                if p.left:
                    stack.append(p.left)
            else:
                p = stack.pop()
                if pre:
                    ans = min(ans, p.val - pre.val)
                    if ans == 0:
                        break
                pre = p
        return ans
    # 递归实现
    # def getMinimumDifference(self, root: [TreeNode]) -> int:
    #     pre = None
    #     ans = 100001
    #     def helper(node: TreeNode):
    #         if not node:
    #             return
    #         if node.left:
    #             helper(node.left)
    #         nonlocal pre
    #         nonlocal ans
    #         if pre:
    #             ans = min(ans, abs(node.val - pre.val))
    #             if ans == 1:
    #                 return
    #         pre = node
    #         if node.right:
    #             helper(node.right)
    #
    #     helper(root)
    #     return ans
