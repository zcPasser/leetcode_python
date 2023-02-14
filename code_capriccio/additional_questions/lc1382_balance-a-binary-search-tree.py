
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.sorted_list = []

    def traversal(self, root: TreeNode):
        if root.left:
            self.traversal(root.left)
        self.sorted_list.append(root.val)
        if root.right:
            self.traversal(root.right)
        return

    def get_sorted_list(self, root):
        self.traversal(root)

    def get_tree(self, left: int, right: int):
        if left > right:
            return None
        mid = (right - left) // 2 + left
        root = TreeNode(self.sorted_list[mid])
        root.left = self.get_tree(left, mid - 1)
        root.right = self.get_tree(mid + 1, right)
        return root


    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.get_sorted_list(root)
        return self.get_tree(0, len(self.sorted_list) - 1)

head = TreeNode(1)
head.right = TreeNode(2)
head.right.right = TreeNode(3)
head.right.right.right = TreeNode(4)
s = Solution()
print(s.balanceBST(head))