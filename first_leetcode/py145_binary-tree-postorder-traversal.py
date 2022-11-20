# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 后序遍历：左子树-右子树-根。
    # 实现步骤：根节点入栈-访问左子树-返回根节点-访问右子树-返回根节点-访问根节点-根节点出栈。
    """
    其中访问节点的类型：
    1、当前经过节点是叶子节点。
    2、当前经过节点的右子节点是上一次访问的节点。
    """
    # 非递归形式。
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        stack_list = []
        res_list = []
        p = root
        # 用于记录上一次访问的节点，和前序遍历不同，其栈中上一个节点并非上一次访问的。
        prev = None
        while p or len(stack_list) > 0:
            while p:
                # 根节点入栈。
                stack_list.append(p)
                # 访问左子树。
                p = p.left
            if len(stack_list) > 0:
                # 返回根节点。
                p = stack_list.pop(-1)
                # 判别 右子树 是否访问。
                # 判断条件：当前节点p 为 其父节点 右孩子。
                if not p.right or p.right == prev:
                    # 已访问右子树，返回根节点，访问根节点，根节点出栈。
                    res_list.append(p.val)
                    prev = p
                    # 此处为了跳过下一次循环的访问左子节点的过程，直接进入栈的弹出阶段，因为但凡在栈中的节点，它们的左子节点都肯定被经过且已放入栈中。
                    p = None
                else:
                    # 不访问节点，则弹回节点。
                    stack_list.append(p)
                    # 访问右子树。
                    p = p.right
        return res_list

    # 递归形式。
    # def postorderTraversal(self, root: TreeNode) -> list[int]:
    #     res_list = []
    #
    #     # 递归函数。
    #     def postorder(root, p_list):
    #         if root:
    #             # 访问左子树。
    #             postorder(root.left, p_list)
    #             # 访问右子树。
    #             postorder(root.right, p_list)
    #             # 访问根节点。
    #             p_list.append(root.val)
    #
    #     postorder(root, res_list)
    #     return res_list


head = TreeNode(1)
p = TreeNode(2)
q = TreeNode(3)
head.right, p.left = p, q
ss = Solution()
print(ss.postorderTraversal(head))
