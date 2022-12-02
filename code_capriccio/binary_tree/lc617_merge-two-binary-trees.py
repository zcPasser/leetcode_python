from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 迭代实现——层序遍历
    def mergeTrees(self, root1: [TreeNode], root2: [TreeNode]) -> [TreeNode]:
        if not root2:
            return root1
        if not root1:
            return root2
        que = deque()
        que.extend([root1, root2])
        while que:
            node1, node2 = que.popleft(), que.popleft()
            # 必然为 非空节点
            node1.val += node2.val
            if node1.left and node2.left:
                que.extend([node1.left, node2.left])
            if node1.right and node2.right:
                que.extend([node1.right, node2.right])
            # 树2左孩子不空，移过去即可，其孩子都一起移过去。
            if not node1.left and node2.left:
                node1.left = node2.left
            if not node1.right and node2.right:
                node1.right = node2.right
            # 至于 树1的孩子为不空，而树2孩子空，则 无须操作，因为是对原来的树1结构进行修改。
        return root1
    # 递归实现——前序遍历
    # def mergeTrees(self, root1: [TreeNode], root2: [TreeNode]) -> [TreeNode]:
    #     def helper(node1: TreeNode, node2: TreeNode):
    #         if not node2:
    #             return node1
    #         if not node1:
    #             return node2
    #         node1.val += node2.val
    #         node1.left = helper(node1.left, node2.left)
    #         node1.right = helper(node1.right, node2.right)
    #         return node1
    #
    #     return helper(root1, root2)
        # def helper(node1: TreeNode, node2: TreeNode):
        #     if not node1 and not node2:
        #         return None
        #     node = TreeNode()
        #     left_1, right_1 = None, None
        #     left_2, right_2 = None, None
        #     if node1:
        #         node.val += node1.val
        #         left_1 = node1.left
        #         right_1 = node1.right
        #     if node2:
        #         node.val += node2.val
        #         left_2 = node2.left
        #         right_2 = node2.right
        #     node.left = helper(left_1, left_2)
        #     node.right = helper(right_1, right_2)
        #     return node
        # return helper(root1, root2)