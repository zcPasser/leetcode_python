from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestNodes(self, root: [TreeNode], queries: list[int]) -> list[list[int]]:
        ans = []
        if root:
            level_traversal = []
            que = deque()
            que.append(root)
            while que:
                size = len(que)
                for _ in range(size):
                    p = que.popleft()
                    if p:
                        level_traversal.append(p.val)
                        if p.left:
                            que.append(p.left)
                        else:
                            que.append(None)
                        if p.right:
                            que.append(p.right)
                        else:
                            que.append(None)
                    else:
                        level_traversal.append(-1)

            len_nodes = len(level_traversal)
        def find_min(num: int):
            i = 0
            min_ = -1
            while i < len_nodes:
                if level_traversal[i] == -1:
                    break
                if level_traversal[i] == num:
                    min_ = num
                    break
                if level_traversal[i] < num:
                    min_ = level_traversal[i]
                    i = 2 * i + 2
                else:
                    i = 2 * i + 1
            return min_
        def find_max(num: int):
            i = 0
            max_ = 1000001
            while i < len_nodes:
                if level_traversal[i] == -1:
                    break
                if level_traversal[i] == num:
                    max_ = num
                    break
                if level_traversal[i] < num:
                    i = 2 * i + 2
                else:
                    max_ = level_traversal[i]
                    i = 2 * i + 1
            return max_
        for num in queries:
            max_min = find_max(root, num)
            ans.append([find_min(root, num), max_min if max_min != 1000001 else -1])
        return ans

    # def closestNodes(self, root: [TreeNode], queries: list[int]) -> list[list[int]]:
    #     ans = []
    #     def find_min(root: TreeNode, num: int) -> int:
    #         if not root:
    #             return -1
    #         if root.val == num:
    #             return num
    #         if root.val < num:
    #             return max(root.val, find_min(root.right, num))
    #         else:
    #             return max(-1, find_min(root.left, num))
    #     def find_max(root: TreeNode, num: int) -> int:
    #         if not root:
    #             return 1000001
    #         if root.val == num:
    #             return num
    #         if root.val < num:
    #             return min(1000001, find_max(root.right, num))
    #         else:
    #             return min(root.val, find_max(root.left, num))
    #     for num in queries:
    #         max_min = find_max(root, num)
    #         ans.append([find_min(root, num), max_min if max_min != 1000001 else -1])
    #     return ans

