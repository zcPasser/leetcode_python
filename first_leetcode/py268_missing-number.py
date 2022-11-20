"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
"""
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums_set = set(nums)
        for i in range(n + 1):
            if i not in nums_set:
                return i


solution = Solution()
nums = [3, 0, 1]
print(solution.missingNumber(nums))
