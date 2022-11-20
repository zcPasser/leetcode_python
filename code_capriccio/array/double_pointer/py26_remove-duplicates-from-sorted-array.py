
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow_idx, fast_idx = 0, 1
        while fast_idx < len(nums):
            if nums[fast_idx] != nums[slow_idx]:
                if fast_idx - slow_idx > 1:
                    nums[slow_idx + 1] = nums[fast_idx]
                slow_idx += 1
            fast_idx += 1

        return slow_idx + 1


nums = [1]
s = Solution()
print(s.removeDuplicates(nums))