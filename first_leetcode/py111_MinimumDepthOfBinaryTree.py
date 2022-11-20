# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 边界
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        depth = 1
        queue_list = []
        queue_list.append([root])
        while len(queue_list) > 0:
            level = queue_list.pop(0)
            next_level = []
            for p in level:
                # 遇到该层叶子
                if p.left is None and p.right is None:
                    return depth
                else:
                    next_level.extend([pp for pp in [p.left, p.right] if pp is not None])
            depth += 1
            queue_list.append(next_level)
        return depth