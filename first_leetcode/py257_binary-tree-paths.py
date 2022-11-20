"""
描述：
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
叶子节点 是指没有子节点的节点。

提示：
1、树中节点的数目在范围 [1, 100] 内
2、-100 <= Node.val <= 100

思路：
1、从 树的 DFS遍历 角度。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        res = []
        stack = []
        last, p = None, root
        while len(stack) > 0 or p:
            if p:
                # 访问 当前 根节点，根节点 入栈。
                stack.append(p)
                # 更新 last指针；进入 左子树。
                last, p = p, p.left
            else:
                p = stack[-1]
                # 自然遍历 导致 p 为 none，栈顶 为 叶子。
                if not p.left and not p.right:
                    # 打印 当前路径。
                    s = ''
                    for node in stack:
                        s += str(node.val) + '->'
                    res.append(s[:-2])
                    # 更新指针，last记录，p置空来返回。
                    last, p = p, None
                    stack.pop()
                # 人为置空 p，旨在 回溯。
                # 从 左子树 返回。
                elif (last == p and not p.left) or (last == p.left):
                    # 更新 指针，last->当前 根节点，p->进入 右子树。
                    last, p = p, p.right
                # 从 右子树 返回。
                elif (last == p and not p.right) or (last == p.right):
                    # 更新指针。
                    last, p = p, None
                    stack.pop()

        return res


import BTree as btree

nodes1 = [1, 2, 5, 3]
nodes2 = [2, 5, 1, 3]
bt = btree.BTree(nodes1=nodes1, nodes2=nodes2)
root = bt.get_root()
solution = Solution()
print(solution.binaryTreePaths(root))
