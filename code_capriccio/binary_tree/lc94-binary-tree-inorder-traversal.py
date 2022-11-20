# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 统一 迭代 实现
    def inorderTraversal(self, root: [TreeNode]) -> list[int]:
        ans = []
        stack_list = []
        if root:
            # 初始化 栈。
            stack_list.append(root)
            while stack_list:
                # 出栈 栈顶节点，避免重复操作。根节点 实则入了2次栈。
                # p 负责 遍历节点,由于 遍历 和 处理 不同步,所以此处出栈.
                p = stack_list.pop()
                # 栈顶节点 非空
                if p:
                    # 添加右节点（空节点不入栈）
                    if p.right:
                        stack_list.append(p.right)
                    # 添加中节点
                    stack_list.append(p)
                    # 中节点访问过，但是还没有处理，加入空节点做为标记。
                    stack_list.append(None)
                    # 添加左节点（空节点不入栈）
                    if p.left:
                        stack_list.append(p.left)
                # 栈顶节点 为 空，即 处理节点的标记。
                else:
                    # 由于 之前的空标记已经出栈,当前栈顶为 待处理的节点,故 出栈处理.
                    p = stack_list.pop()
                    # 处理,即 加入结果集.
                    ans.append(p.val)
        return ans
    # 迭代 实现
    # def inorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     cur = root
    #     stack_list = []
    #     ans = []
    #     while cur or stack_list:
    #         # cur指针 负责遍历，直到当前树的最左节点。
    #         if cur:
    #             stack_list.append(cur)
    #             cur = cur.left
    #         else:
    #             # 栈 负责处理 节点——栈 弹出的节点。
    #             cur = stack_list.pop()
    #             # 具体处理 根节点。
    #             ans.append(cur.val)
    #             # 指针 遍历 右子树。
    #             cur = cur.right
    #     return ans
    # 递归 实现
    # def inorderTraversal(self, root: [TreeNode]) -> list[int]:
    #     ans = []
    #     def traversal(r: [TreeNode]):
    #         if not r:
    #             return
    #         traversal(r.left)
    #         ans.append(r.val)
    #         traversal(r.right)
    #
    #     traversal(root)
    #     return ans