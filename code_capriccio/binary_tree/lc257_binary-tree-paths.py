# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代实现——前序遍历 + 统一形式 + 隐形回溯
    def binaryTreePaths(self, root: [TreeNode]) -> list[str]:
        ans = []
        if root:
            # 一个栈：同时入栈 当前节点 + 到当前节点的路径。
            stack = [root, str(root.val)]
            while stack:
                # 出栈 当前节点 + 到此的路径
                path = stack.pop()
                p = stack.pop()
                # 终止条件
                if not p.left and not p.right:
                    ans.append(path)
                if p.right:
                    stack.append(p.right)
                    stack.append(path + '->' + str(p.right.val))
                if p.left:
                    stack.append(p.left)
                    stack.append(path + '->' + str(p.left.val))

        return ans
    # 递归实现——前序遍历 + 隐形回溯
    def binaryTreePaths(self, root: [TreeNode]) -> list[str]:
        ans = []
        def helper(node: TreeNode, path: str):
            path += str(node.val)
            if not node.left and not node.right:
                ans.append(path)
                return
            if node.left:
                # 通过传参，间接实现回溯
                # 因为 当前递归中的path的值 并没有改变，在给下一层传参是给了一个连接，新的path_
                helper(node.left, path + '->')
            if node.right:
                helper(node.right, path + '->')
            return
        if root:
            helper(root, '')
        return ans
    # 递归实现——前序遍历
    def binaryTreePaths(self, root: [TreeNode]) -> list[str]:
        ans = []
        # 记录 当前路径
        path = []
        # 三部曲——参数：当前节点
        def helper(node: TreeNode):
            # 处理 中
            # 放在前面，是由于 当遇到终止条件返回前，当前路径的最后节点要事先在path中。
            path.append(node.val)
            # 三部曲——终止条件：遇到叶子节点结束。
            # 不是 遇到空节点，是因为 在进入递归前 对空节点已经进行了 过滤。
            if not node.left and not node.right:
                # 终止条件处理：记录 当前路径。
                ans.append('->'.join([str(v) for v in path]))
                return
            # 处理 左
            # 对 空节点 过滤
            if node.left:
                helper(node.left)
                # 进行 回溯
                path.pop()
            # 处理 右
            if node.right:
                helper(node.right)
                # 进行 回溯
                path.pop()
            return
        if root:
            helper(root)
        return ans
