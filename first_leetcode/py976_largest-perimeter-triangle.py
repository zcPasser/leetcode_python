

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        for i in range(len(nums) - 1, 1, -1):
            if nums[i] < (nums[i - 1] + nums[i - 2]):
                return nums[i] + nums[i - 1] + nums[i - 2]

        return 0


nums = [2, 1, 2]
print(nums[2:: -1])
s = Solution()
print(s.largestPerimeter(nums))

