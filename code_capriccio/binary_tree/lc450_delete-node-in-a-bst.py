# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: [TreeNode], key: int) -> [TreeNode]:
        def helper(node: TreeNode, k: int) -> [TreeNode]:
            if not node:
                return None
            if node.val == k:
                if not node.left and not node.right:
                    return None
                elif not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    cur = node.right
                    while cur.left:
                        cur = cur.left
                    cur.left = node.left
                    return node.right
            elif node.val < k:
                node.right = helper(node.right, k)
            else:
                node.left = helper(node.left, k)

            return node
        return helper(root, key)

k = 3
r = TreeNode(5)
r.left = TreeNode(3)
r.right = TreeNode(6)
r.left.left = TreeNode(2)
r.left.right = TreeNode(4)
r.right.right = TreeNode(7)
s = Solution()
print(s.deleteNode(r, k))

