# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> [TreeNode]:
        # 递归三部曲——参数：当前子树的中序数组的begin与end 和 前序数组的begin与end。(遵循[begin, end))
        def helper(inorder_begin: int, inorder_end: int, preorder_begin: int, preorder_end: int) -> [TreeNode]:
            # 通过前序数组 找到 当前根节点。
            # 递归三部曲——终止条件：根节点为空。
            # 前序数组 为空，即 当前子树空节点
            # 由于[begin, end)，空节点形式为 begin==end
            if preorder_begin == preorder_end:
                return None
            root_val = preorder[preorder_begin]
            root = TreeNode(root_val)
            # 递归三部曲——终止条件：根节点 为 叶子节点。
            if preorder_end - 1 == preorder_begin:
                return root
            # 根据根节点，在中序数组中获取切分点。
            delimeter_idx = 0
            for i in range(inorder_begin, inorder_end):
                if inorder[i] == root_val:
                    delimeter_idx = i
            # 递归三部曲——单层逻辑
            # 对 中序数组 进行切分。
            # 当前根节点的左子树中序数组 begin 和 end
            left_inorder_begin = inorder_begin
            # 右开
            left_inorder_end = delimeter_idx
            # 当前根节点的右子树子树中序数组
            right_inorder_begin = delimeter_idx + 1
            right_inorder_end = inorder_end
            # 对 前序数组 进行切分。
            # 依据 左右子树长度 在 两种遍历中不变。
            left_preorder_begin = preorder_begin + 1
            left_preorder_end = left_preorder_begin + delimeter_idx - left_inorder_begin
            right_preorder_begin = left_preorder_end
            right_preorder_end = preorder_end
            # 递归实现左子树、右子树 构造
            root.left = helper(left_inorder_begin, left_inorder_end, left_preorder_begin, left_preorder_end)
            root.right = helper(right_inorder_begin, right_inorder_end, right_preorder_begin, right_preorder_end)

            return root
        len_nodes = len(inorder)
        if len_nodes == 0:
            return None
        return helper(0, len_nodes, 0, len_nodes)