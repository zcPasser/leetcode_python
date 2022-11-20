

class Solution:
    def smallestRangeI(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        mid = (nums[0] + nums[-1]) // 2
        if (mid - nums[0] <= k) and (nums[-1] - mid <= k):
            return 0
        else:
            return nums[-1] - nums[0] - 2 * k


nums = [3, 1, 10]
k = 4
s = Solution()
print(s.smallestRangeI(nums, k))
