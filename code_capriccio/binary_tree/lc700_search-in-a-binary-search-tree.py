# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 迭代实现
    def searchBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        p = root
        ans = None
        while p:
            if p.val == val:
                ans = p
                break
            elif p.val < val:
                p = p.right
            else:
                p = p.left

        return ans
    # 递归实现
    # def searchBST(self, root: [TreeNode], val: int) -> [TreeNode]:
    #     def helper(node: TreeNode, val: int):
    #         if node.val == val:
    #             return node
    #         ans = None
    #         if node.val < val and node.right:
    #             ans = helper(node.right, val)
    #         if node.val > val and node.left:
    #             ans = helper(node.left, val)
    #         return ans
    #     ans = None
    #     if root:
    #         ans = helper(root, val)
    #     return ans