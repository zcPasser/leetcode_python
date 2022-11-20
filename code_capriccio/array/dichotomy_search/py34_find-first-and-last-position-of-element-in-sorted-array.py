
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                while l < mid and nums[l] != target:
                    l += 1
                while r > mid and nums[r] != target:
                    r -= 1
                return [l, r]
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [-1, -1]


nums = []
target = 6
s = Solution()
print(s.searchRange(nums, target))