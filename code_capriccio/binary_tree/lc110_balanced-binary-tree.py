# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代实现——栈 模拟 后序遍历
    def isBalanced(self, root: [TreeNode]) -> bool:
        def helper(node: TreeNode) -> int:
            ans = 0
            if node:
                # 后序遍历，迭代实现——统一形式
                stack = [root]
                depth = 0
                while stack:
                    pp = stack.pop()
                    if pp:
                        stack.append(pp)
                        stack.append(None)
                        depth += 1
                        if pp.right:
                            stack.append(pp.right)
                        if pp.left:
                            stack.append(pp.left)
                    else:
                        pp = stack.pop()
                        depth -= 1
                    ans = max(ans, depth)
            return ans
        if root:
            stack_ = [root]
            while stack_:
                p = stack_.pop()
                if abs(helper(p.left) - helper(p.right)) > 1:
                    return False
                if p.right:
                    stack_.append(p.right)
                if p.left:
                    stack_.append(p.left)

        return True
    # 递归实现——后序遍历+求高度模板
    # def isBalanced(self, root: [TreeNode]) -> bool:
    #     # 递归三部曲——参数：当前子树根节点；返回值：当前子树的高度(PS：若是 返回值=-1，则 当前子树为 非平衡二叉树。)。
    #     def helper(node: TreeNode) -> int:
    #         # 递归三部曲——终止条件：当前根节点为空，则 返回高度为0
    #         if not node:
    #             return 0
    #         # 递归三部曲——单层逻辑
    #         # 处理 左
    #         left_height = helper(node.left)
    #         # 若是 左子树 已经不平衡，则 终止并返回-1
    #         if left_height == -1:
    #             return -1
    #         # 处理 右
    #         right_height = helper(node.right)
    #         if right_height == -1:
    #             return -1
    #         # 处理 中
    #         # 当前子树为 非平衡二叉树
    #         if abs(left_height - right_height) > 1:
    #             ans = -1
    #         # 当前子树 为 平衡二叉树，记录 其高度。
    #         else:
    #             ans = 1 + max(left_height, right_height)
    #         return ans
    #     return False if helper(root) == -1 else True
