from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # DFS、后序遍历
    def maxDepth(self, root: 'Node') -> int:
        def get_height(node: Node) -> int:
            if not node:
                return 0
            max_child_height = 0
            for child in node.children:
                max_child_height = max(max_child_height, get_height(child))
            return 1 + max_child_height
        return get_height(root)
    # BFS、层次遍历
    # def maxDepth(self, root: 'Node') -> int:
    #     ans = 0
    #     if root:
    #         que = deque()
    #         que.append(root)
    #         while que:
    #             size = len(que)
    #             ans += 1
    #             for _ in range(size):
    #                 p = que.popleft()
    #                 for child in p.children:
    #                     if child:
    #                         que.append(child)
    #     return ans


