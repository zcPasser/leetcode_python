# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> [TreeNode]:
        def helper(left: int, right: int) -> [TreeNode]:
            if left > right:
                return None
            mid = (right - left) // 2 + left
            node = TreeNode(nums[mid])
            node.left = helper(left, mid - 1)
            node.right = helper(mid + 1, right)

            return node
        return helper(0, len(nums) - 1)
