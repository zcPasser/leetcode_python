# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> [TreeNode]:
        def helper(begin: int, end: int):
            if begin >= end:
                return None
            max_idx = begin
            for i in range(begin + 1, end):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            root = TreeNode(nums[max_idx])
            if end - begin > 1:
                left_begin = begin
                left_end = max_idx

                right_begin = max_idx + 1
                right_end = end

                root.left = helper(left_begin, left_end)
                root.right = helper(right_begin, right_end)
            return root
        return helper(0, len(nums))

nums = [3,2,1,6,0,5]
s = Solution()
print(s.constructMaximumBinaryTree(nums))