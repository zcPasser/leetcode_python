# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        if root:
            stack_list = []
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
                    p.left, p.right = p.right, p.left

        return root
