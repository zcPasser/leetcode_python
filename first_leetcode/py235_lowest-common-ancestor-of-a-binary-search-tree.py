# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
关键：二叉搜索树BST。
"""
class Solution:
    # DFS遍历，记录分别到节点 p、q的路径，类似比较最长公共前缀的最后一个字符。
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search_BST(root: TreeNode, target: TreeNode) -> list:
            path = []
            t = root
            while t.val != target.val:
                path.append(t)
                if t.val < target.val:
                    t = t.right
                else:
                    t = t.left
            path.append(t)
            return path

        path_p = search_BST(root, target=p)
        path_q = search_BST(root, target=q)

        near_ancestor = None
        for u, v in zip(path_p, path_q):
            if u == v:
                near_ancestor = u
            else:
                break

        return near_ancestor

import BTree
nodes1 = [6, 2, 0, 4, 3, 5, 8, 7, 9]
nodes2 = [0, 2, 3, 4, 5, 6, 7, 8, 9]

tree = BTree.BTree(nodes1, nodes2)
ss = Solution()
print(ss.lowestCommonAncestor(root=tree.root, p=TreeNode(2), q=TreeNode(8)))


