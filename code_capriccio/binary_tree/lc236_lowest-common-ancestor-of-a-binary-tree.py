# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 三部曲——参数：中节点+子节点；返回值：当前子树若有公共祖先则返回该祖先，否则返回 空。
        def helper(node: TreeNode, pp: TreeNode, qq: TreeNode) -> [TreeNode]:
            # 三部曲——终止条件：当前中节点就是 目标节点（可能目标节点本身是祖先），返回，否则 若中节点为空 返回空。
            if node == p or node == q or not node:
                return node
            # 三部曲——单层逻辑
            # 搜索整棵树的写法，需要 用变量存放返回值，进行处理
            left = helper(node.left, pp, qq)
            right = helper(node.right, pp, qq)
            # 左右子树都不空，找到 最近公共祖先。
            if left and right:
                return node
            # 在其中一棵树中。
            elif left and not right:
                return left
            elif not left and right:
                return right
            else:
                return None
        return helper(root, p, q)