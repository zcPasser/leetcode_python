from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 递归实现——普通二叉树+中序遍历
    def findMode(self, root: [TreeNode]) -> list[int]:
        ans = []
        if not root:
            return ans
        pre = None
        cnt = 0
        max_cnt = 0
        def helper(node: TreeNode):
            if not node:
                return
            if node.left:
                helper(node.left)
            nonlocal pre
            nonlocal cnt
            nonlocal max_cnt
            if pre:
                if pre.val == node.val:
                    cnt += 1
                else:
                    cnt = 1
            else:
                cnt = 1
            if cnt == max_cnt:
                ans.append(node.val)
            elif cnt > max_cnt:
                ans.clear()
                ans.append(node.val)
                max_cnt = cnt
            pre = node
            if node.right:
                helper(node.right)
            return
        helper(root)
        return ans


    # 递归实现——普通二叉树+中序遍历
    # def findMode(self, root: [TreeNode]) -> list[int]:
    #     ans = []
    #     if not root:
    #         return ans
    #     cnt = Counter()
    #     def helper(node: TreeNode):
    #         if not node:
    #             return
    #         if node.left:
    #             helper(node.left)
    #         cnt[node.val] += 1
    #         if node.right:
    #             helper(node.right)
    #         return
    #     helper(root)
    #     max_nums = root.val
    #     for val, nums in cnt.items():
    #         if nums > cnt[max_nums]:
    #             ans.clear()
    #             ans.append(val)
    #             max_nums = val
    #         elif nums == cnt[max_nums]:
    #             ans.append(val)
    #     return ans


root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(2)
s = Solution()
print(s.findMode(root))