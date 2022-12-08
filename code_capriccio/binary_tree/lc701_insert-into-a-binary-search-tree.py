# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代实现——二叉搜索树的迭代，注意结合 pre + cur
    def insertIntoBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        node = TreeNode(val)
        if not root:
            return node
        pre = None
        cur = root
        while cur:
            pre = cur
            if cur.val < val:
                cur = cur.right
            else:
                cur = cur.left

        if pre.val < val:
            pre.right = node
        else:
            pre.left = node
        return root
    # 递归实现——有返回值
    def insertIntoBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        def helper(node: TreeNode, val: int) -> TreeNode:
            if not node:
                node = TreeNode(val)
                return node
            if node.val < val:
                node.right = helper(node.right, val)
            if node.val > val:
                node.left = helper(node.left, val)
            return node
        return helper(root, val)
    # 递归实现——无返回值
    def insertIntoBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        def helper(node: TreeNode, val: int):
            if node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                    return
                else:
                    helper(node.right, val)
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    return
                else:
                    helper(node.left, val)
            return
        if root:
            helper(root, val)
        else:
            root = TreeNode(val)
        return root