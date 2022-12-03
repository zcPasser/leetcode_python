# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 迭代实现——中序遍历+统一形式
    def isValidBST(self, root: [TreeNode]) -> bool:
        if root:
            stack = [root]
            pre = None
            while stack:
                p = stack.pop()
                # 负责遍历
                if p:
                    if p.right:
                        stack.append(p.right)
                    stack.append(p)
                    stack.append(None)
                    if p.left:
                        stack.append(p.left)
                # 负责处理中节点 逻辑
                else:
                    p = stack.pop()
                    if pre and pre.val >= p.val:
                        return False
                    pre = p
        return True

    # 递归实现——中序遍历
    # def isValidBST(self, root: [TreeNode]) -> bool:
    #     pre = None
    #     def helper(node: TreeNode) -> bool:
    #         if not node:
    #             return True
    #         nonlocal pre
    #         left = helper(node.left)
    #         if pre and pre.val >= node.val:
    #             return False
    #         pre = node
    #         right = helper(node.right)
    #         return left and right
    #     return helper(root)
    # def isValidBST(self, root: [TreeNode]) -> bool:
    #     inorder_seq = []
    #     def helper(node: TreeNode):
    #         if not node:
    #             return
    #         helper(node.left)
    #         inorder_seq.append(node.val)
    #         helper(node.right)
    #     helper(root)
    #     for i in range(1, len(inorder_seq)):
    #         if inorder_seq[i] <= inorder_seq[i - 1]:
    #             return False
    #     return True

root = TreeNode(1)
root.left = TreeNode(1)
s = Solution()
print(s.isValidBST(root))