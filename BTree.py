"""
根据 遍历序列，创建 二叉树。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BTree:
    def __int__(self):
        self.root = None

    def __init__(self, nodes1: list, nodes2: list):
        self.root = self.createBTree(nodes1, nodes2)

    # 根据 中序遍历 & 先序遍历，递归 创建 二叉树。
    def createBTree(self, nodes1: list, nodes2: list):
        # 递归边界。
        if len(nodes1) == 0 or len(nodes2) == 0:
            return None
        # 创建当前 二叉树根节点。
        root = TreeNode(nodes1[0])
        # 获取 当前根节点 在 中序遍历 中的 索引。
        i = nodes2.index(nodes1[0])
        # 根据索引，划分 当前左子树、右子树。
        len_left_child_tree = len(nodes2[:i])

        root.left = self.createBTree(nodes1[1: len_left_child_tree + 1], nodes2[:i])
        root.right = self.createBTree(nodes1[len_left_child_tree + 1:], nodes2[i + 1:])

        return root

    # 获取 根。
    def get_root(self):
        return self.root

    # 层次遍历 打印 二叉树。
    def print_by_hierarchical_traversal(self):
        queue_list = []
        p = self.root
        s = ''
        if not p:
            return s
        queue_list.append(p)
        while len(queue_list) > 0 or p:
            p = queue_list.pop(0)
            s += str(p.val) + '  '
            if p.left:
                queue_list.append(p.left)
            if p.right:
                queue_list.append(p.right)
            p = None
        return s




# nodes1 = [2, 1, 4, 3, 6, 5]
# nodes2 = [4, 1, 2, 3, 5, 6]
# btree = BTree(nodes1, nodes2)
# print(btree.print_by_hierarchical_traversal())