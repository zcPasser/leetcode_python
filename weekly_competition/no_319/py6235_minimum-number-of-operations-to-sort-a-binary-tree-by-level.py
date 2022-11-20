import math
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minimumOperations(self, root: [TreeNode]) -> int:
        # 层次遍历，以完全二叉树形式 用数组保存节点，包括 空节点，记为0.
        complete_binary_tree = []
        que = deque()
        que.append(root)
        complete_binary_tree.append(root.val)
        while que:
            p = que.popleft()
            if p.left:
                que.append(p.left)
                complete_binary_tree.append(p.left.val)
            else:
                complete_binary_tree.append(0)
            if p.right:
                que.append(p.right)
                complete_binary_tree.append(p.right.val)
            else:
                complete_binary_tree.append(0)
        # 获取 层数
        levels = math.floor(math.log2(len(complete_binary_tree))) + 1
        # 获取 序列成为 严格递增序列 的 最小操作次数。
        def get_min_cnts(nums: list[int]) -> int:
            ans = 0
            return ans
        ans = 0
        # 根据 层数 划分每层序列
        for level in range(levels):
            # 获取 当前层序列。
            # 区间左闭右开：[,)
            nums = [num for num in complete_binary_tree[math.pow(2, level) - 1: math.pow(2, level + 1) - 1] if num != 0]
            ans += get_min_cnts(nums)

        return ans
