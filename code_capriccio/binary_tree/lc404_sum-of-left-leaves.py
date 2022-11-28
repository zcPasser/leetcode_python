# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代实现——后续遍历+统一形式
    def sumOfLeftLeaves(self, root: [TreeNode]) -> int:
        ans = 0
        if root:
            stack = [root]
            while stack:
                p = stack.pop()
                if p:
                    stack.append(p)
                    stack.append(None)
                    if p.right:
                        stack.append(p.right)
                    if p.left:
                        stack.append(p.left)
                else:
                    p = stack.pop()
                    if p.left and not p.left.left and not p.left.right:
                        ans += p.left.val
        return ans
    # 递归实现——后续遍历
    def sumOfLeftLeaves(self, root: [TreeNode]) -> int:
        # 三部曲——参数：当前根节点
        # 三部曲——返回值：当前根节点的左子树和右子树的 所有 左叶子值之和。
        def helper(node: TreeNode) -> int:
            # 终止条件：遇到 空节点，其左叶子也为空，对求和贡献为0.
            if not node:
                return 0
            # 终止条件2：遇到叶子节点，避免 多做一层无用遍历。
            if not node.left and not node.right:
                return 0
            # 单层逻辑：目标 左叶子 必须 通过父节点 判断。
            # 处理 左.
            # 遇到 合法左叶子，计算,否则 进入左子树。
            if node.left and not node.left.left and not node.left.right:
                left_val = node.left.val
            else:
                left_val = helper(node.left)
            # 处理 右
            # 获取 右子树的 左叶子 之和.
            right_val = helper(node.right)
            # 处理 中.
            sum_val = left_val + right_val
            return sum_val

        return helper(root)
