from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        ans = []
        if root:
            que = deque()
            que.append(root)
            while que:
                size = len(que)
                cur_level = []
                for _ in range(size):
                    p = que.popleft()
                    cur_level.append(p.val)
                    # cur.children 是 Node 对象组成的列表，也可能为 None
                    if p.children:
                        que.extend(p.children)
                ans.append(cur_level)
        return ans