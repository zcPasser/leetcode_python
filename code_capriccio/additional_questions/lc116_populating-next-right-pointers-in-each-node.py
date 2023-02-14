from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution:
    def traversal(self, root: 'Node'):
        if not root:
            return
        if not root.left:
            root.left.next = root.right

        if not root.right:
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None

        self.traversal(root.left)
        self.traversal(root.right)
        return

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            self.traversal(root)

        return root

    # 迭代
    # def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    #     if not root:
    #         return None
    #     que = deque()
    #     que.append(root)
    #     while que:
    #         len_level = len(que)
    #         last = None
    #         for i in range(len_level):
    #             p = que.popleft()
    #             if last:
    #                 last.next = p
    #             last = p
    #             if p.left:
    #                 que.append(p.left)
    #             if p.right:
    #                 que.append(p.right)
    #         last.next = None
    #     return root
