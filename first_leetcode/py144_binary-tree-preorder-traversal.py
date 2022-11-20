# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 前序遍历步骤：访问根节点-根节点入栈-访问左子树-回到根节点-根节点出栈-访问右子树。
    # 前序遍历——非递归形式。
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        stack_list = []
        res_list = []
        p = root
        while p or len(stack_list) > 0:
            while p:
                # 访问根节点。
                res_list.append(p.val)
                # 根节点 入栈。
                stack_list.append(p)
                # 访问左子树。
                p = p.left
            if len(stack_list) > 0:
                # 回到根节点，根节点出栈。
                p = stack_list.pop(-1)
                # 判别 右子树 是否访问。
                # 判断条件：当前节点p 为 其父节点 右孩子。
                if stack_list[-1].right == p:
                    # 已访问右子树，置空p，继续出栈。
                    p = None
                else:
                    # 访问右子树。
                    p = p.right
        return res_list



    # 前序遍历——递归形式。
    # def preorderTraversal(self, root: TreeNode) -> list[int]:
    #     preporder_list = []
    #     def preporder(root, p_list):
    #         if root:
    #             # 先序：根-左-右。
    #             p_list.append(root.val)
    #             preporder(root.left, p_list)
    #             preporder(root.right, p_list)
    #
    #     preporder(root, preporder_list)
    #     return preporder_list


