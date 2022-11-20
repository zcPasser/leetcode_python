from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            que = deque()
            que.append(root)
            while que:
                size = len(que)
                last = None
                for i in range(size):
                    p = que.popleft()
                    if p.left:
                        que.append(p.left)
                    if p.right:
                        que.append(p.right)
                    if i > 0:
                        last.next = p
                    last = p
                last.next = None

        return root