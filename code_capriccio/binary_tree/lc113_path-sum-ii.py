# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 递归实现——前序遍历（实则无所谓何种遍历，因为 没有对中节点处理的逻辑）
    def pathSum(self, root: [TreeNode], targetSum: int) -> list[list[int]]:
        ans = []
        path = []
        # 递归三部曲——参数：当前根节点、计数器；——返回值：没有返回值，由于需要 搜索整棵树。
        def helper(node: TreeNode, cnt: int):
            # 三部曲——终止条件：叶子节点，返回。
            if not node.left and not node.right:
                # 若当 计数器==0（减法），ans 加入 当前完整路径的拷贝（PS：拷贝）。
                if cnt == 0:
                    ans.append(path[:])
                return
            # 三部曲——单层逻辑：前序遍历（缺失 处理中节点）
            # 处理 左（过滤空节点）
            if node.left:
                # 当前路径path 更新
                path.append(node.left.val)
                # 左递归
                # 计数器 传参 实现 回溯
                helper(node.left, cnt - node.left.val)
                # 对当前路径path出栈，实现回溯
                path.pop()
            if node.right:
                path.append(node.right.val)
                helper(node.right, cnt - node.right.val)
                path.pop()
        if root:
            path.append(root.val)
            helper(root, targetSum - root.val)
        return ans


