# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> [TreeNode]:
        # 反复于如下步骤
        # step1：找到后序数组的最后节点，即 当前子树的根节点。
        # step2：根据根节点，对 中序数组切分，得到 左子树中序数组 和 右子树中序数组。
        # step3：根据 左子树数组 和 右子树数组长度 各自在不同遍历中相同，由此 在后序数组中 切分出 左子树后序数组 和 右子树后序数组。

        # 处理中 始终遵循 区间左闭右开[begin, end)

        # 递归三部曲——参数：当前子树的中序数组的begin与end 和 后序数组的begin与end。(遵循[begin, end))
        def helper(inorder_begin: int, inorder_end: int, postorder_begin: int, postorder_end: int) -> [TreeNode]:
            # 通过后序数组 找到 当前根节点。
            # 递归三部曲——终止条件：根节点为空。
            # 后序数组 为空，即 当前子树空节点
            # 由于[begin, end)，空节点形式为 begin==end
            if postorder_begin == postorder_end:
                return None
            root_val = postorder[postorder_end - 1]
            root = TreeNode(root_val)
            # 递归三部曲——终止条件：根节点 为 叶子节点。
            if postorder_end - 1 == postorder_begin:
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
            # 对 后序数组 进行切分。
            # 依据 左右子树长度 在 两种遍历中不变。
            left_postorder_begin = postorder_begin
            left_postorder_end = postorder_begin + delimeter_idx - left_inorder_begin
            right_postorder_begin = left_postorder_end
            right_postorder_end = postorder_end - 1
            # 递归实现左子树、右子树 构造
            root.left = helper(left_inorder_begin, left_inorder_end, left_postorder_begin, left_postorder_end)
            root.right = helper(right_inorder_begin, right_inorder_end, right_postorder_begin, right_postorder_end)

            return root
        len_nodes = len(inorder)
        if len_nodes == 0:
            return None
        return helper(0, len_nodes, 0, len_nodes)
