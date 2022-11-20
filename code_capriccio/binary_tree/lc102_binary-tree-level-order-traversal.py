# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 层次遍历——递归实现
    def levelOrder(self, root: [TreeNode]) -> list[list[int]]:
        ans = []
        def helper(root_: TreeNode, depth: int):
            if not root_:
                return
            # 当前节点 所在层数 == ans中层数，即 需要 在结果集ans中 创建depth所在层 的 子结果集。
            if len(ans) == depth:
                ans.append([])
            # 处理当前 节点，即 加入 depth所在 子结果集。
            ans[depth].append(root_.val)
            # 遍历 下一层。
            if root_.left:
                helper(root_.left, depth + 1)
            if root_.right:
                helper(root_.right, depth + 1)
        helper(root, 0)
        return ans

    # 层次遍历——迭代实现
    # def levelOrder(self, root: [TreeNode]) -> list[list[int]]:
    #     ans = []
    #     if root:
    #         # 双端队列 底层容器实现 队列。
    #         que = deque()
    #         # 初始化 队列
    #         que.append(root)
    #         while que:
    #             # 获得 当前层 的 大小，便于分层 处理 节点。
    #             # 这里一定要使用固定大小size，不要使用que.size()，因为que.size是不断变化的
    #             size = len(que)
    #             # 处理 节点，存放 当前层 节点。
    #             cur_level = []
    #             # 对 当前层 所有节点 逐个 遍历。
    #             for _ in range(size):
    #                 # 队列 队头元素 出队
    #                 p = que.popleft()
    #                 # 处理 节点——即 加入 当前层的 结果集
    #                 cur_level.append(p.val)
    #                 # 遍历 当前节点的左孩子，基于队列的性质，FIFO。
    #                 if p.left:
    #                     que.append(p.left)
    #                 # 遍历 当前节点 的右孩子。
    #                 if p.right:
    #                     que.append(p.right)
    #             ans.append(cur_level)
    #     return ans